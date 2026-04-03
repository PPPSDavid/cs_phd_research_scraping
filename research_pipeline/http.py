from __future__ import annotations

import ssl
import threading
import time
import urllib.error
import urllib.request
import urllib.robotparser
from dataclasses import dataclass
from typing import Any
from urllib.parse import urlparse

from research_pipeline.config import get_config_value


@dataclass(frozen=True)
class HttpResponse:
    final_url: str
    text: str


class RobotsAwareHttpClient:
    def __init__(self) -> None:
        self.user_agent = str(get_config_value("http.user_agent", "cs-phd-research-scraping/1.0"))
        self.timeout_seconds = int(get_config_value("http.timeout_seconds", 20))
        self.retry_attempts = int(get_config_value("http.retry_attempts", 3))
        self.retry_backoff_seconds = float(get_config_value("http.retry_backoff_seconds", 1.5))
        self.default_crawl_delay_seconds = float(get_config_value("http.default_crawl_delay_seconds", 1.0))
        self.obey_robots = bool(get_config_value("http.obey_robots", True))
        self.allow_insecure_ssl_retry = bool(get_config_value("http.allow_insecure_ssl_retry", True))
        self.robots_unavailable_policy = str(get_config_value("http.robots_unavailable_policy", "allow"))
        self._robot_parsers: dict[str, urllib.robotparser.RobotFileParser | None] = {}
        self._last_request_time: dict[str, float] = {}
        self._cache: dict[str, HttpResponse] = {}
        self._lock = threading.Lock()

    def fetch_text(self, url: str) -> str:
        return self.fetch_response(url).text

    def fetch_response(self, url: str) -> HttpResponse:
        with self._lock:
            if url in self._cache:
                return self._cache[url]

        host_key = self._host_key(url)
        if self.obey_robots and not self._can_fetch(url):
            raise RuntimeError(f"Blocked by robots.txt policy for {url}")

        last_error: Exception | None = None
        for attempt in range(self.retry_attempts):
            self._throttle(host_key, url)
            try:
                response = self._open(url)
                with self._lock:
                    self._cache[url] = response
                return response
            except Exception as exc:
                last_error = exc
                if attempt + 1 < self.retry_attempts:
                    time.sleep(self.retry_backoff_seconds * (attempt + 1))
        raise RuntimeError(f"Failed to fetch {url}: {last_error}")

    def _open(self, url: str) -> HttpResponse:
        request = urllib.request.Request(url, headers={"User-Agent": self.user_agent})
        try:
            with urllib.request.urlopen(request, timeout=self.timeout_seconds) as response:
                charset = response.headers.get_content_charset() or "utf-8"
                return HttpResponse(
                    final_url=response.geturl(),
                    text=response.read().decode(charset, errors="replace"),
                )
        except urllib.error.URLError as exc:
            reason = getattr(exc, "reason", None)
            if self.allow_insecure_ssl_retry and isinstance(reason, ssl.SSLCertVerificationError):
                with urllib.request.urlopen(
                    request,
                    timeout=self.timeout_seconds,
                    context=ssl._create_unverified_context(),
                ) as response:
                    charset = response.headers.get_content_charset() or "utf-8"
                    return HttpResponse(
                        final_url=response.geturl(),
                        text=response.read().decode(charset, errors="replace"),
                    )
            raise

    def _host_key(self, url: str) -> str:
        parsed = urlparse(url)
        return f"{parsed.scheme}://{parsed.netloc}"

    def _get_robot_parser(self, url: str) -> urllib.robotparser.RobotFileParser | None:
        host_key = self._host_key(url)
        with self._lock:
            if host_key in self._robot_parsers:
                return self._robot_parsers[host_key]

        robots_url = f"{host_key}/robots.txt"
        parser = urllib.robotparser.RobotFileParser()
        parser.set_url(robots_url)
        try:
            parser.read()
        except Exception:
            parser = None

        with self._lock:
            self._robot_parsers[host_key] = parser
        return parser

    def _can_fetch(self, url: str) -> bool:
        parser = self._get_robot_parser(url)
        if parser is None:
            return self.robots_unavailable_policy == "allow"
        return parser.can_fetch(self.user_agent, url)

    def _crawl_delay(self, url: str) -> float:
        parser = self._get_robot_parser(url)
        if parser is None:
            return self.default_crawl_delay_seconds
        delay = parser.crawl_delay(self.user_agent)
        if delay is None:
            delay = parser.crawl_delay("*")
        if delay is None:
            delay = self.default_crawl_delay_seconds
        return float(delay)

    def _throttle(self, host_key: str, url: str) -> None:
        delay = self._crawl_delay(url)
        with self._lock:
            last = self._last_request_time.get(host_key)
            now = time.time()
            if last is not None:
                sleep_time = delay - (now - last)
                if sleep_time > 0:
                    time.sleep(sleep_time)
            self._last_request_time[host_key] = time.time()


_CLIENT: RobotsAwareHttpClient | None = None


def get_http_client() -> RobotsAwareHttpClient:
    global _CLIENT
    if _CLIENT is None:
        _CLIENT = RobotsAwareHttpClient()
    return _CLIENT
