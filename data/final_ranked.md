# Final Ranked Faculty

Sorted by `phd_score` descending, then `ra_score` descending, then school rank ascending.

## Strict Scoring Prompt

```text
You are scoring a professor for:
1. PhD advisor fit
2. RA / pre-PhD lab opportunity fit

You will receive only structured evidence.
Do not infer facts not present in the evidence.
If evidence is insufficient, say UNKNOWN and lower confidence.

User profile:
- Master of Data Science, University of Michigan Ann Arbor
- interests: AI for science, inverse problems, AI for drug discovery, medical imaging, computational biology / bioinformatics

Output schema:
- summary
- phd_score (0-100)
- ra_score (0-100)
- rationale_phd
- rationale_ra
- potential_concerns
- confidence

Strict scoring rules:
- Base all judgments only on research_description, research_tags, recent_work_cues, ra_opportunity_cues, advising_cues, source_type, notes, school_name, and department.
- Give the strongest positive weight to explicit overlap with computational biology, bioinformatics, medical imaging, inverse problems, AI for science, scientific machine learning, drug discovery, molecular design, proteins, genomics, or biomedical imaging.
- Give moderate positive weight to general AI / ML / vision evidence when the user's highest-priority domains are not explicit.
- Give low positive weight to NLP / language-model-only evidence, since it is adjacent but not central to the stated goals.
- Increase PhD fit when advising cues are explicit.
- Increase RA fit when RA / recruiting / prospective-student cues are explicit.
- Increase both scores slightly when recent work cues are explicit.
- Penalize confidence and mention concerns when evidence is sparse, indirect, or mostly UNKNOWN.
- Do not invent advisor availability, funding, lab size, or project details.
```

## Prompt Usage Examples

### Strong direct match

- Input summary: `{"research_tags": "computational biology; medical imaging; machine learning", "research_description": "Research focuses on machine learning for biomedical imaging and computational biology.", "recent_work_cues": "Recent publications in 2025 and 2026 are listed.", "ra_opportunity_cues": "The page explicitly says the lab is recruiting research assistants.", "advising_cues": "The page explicitly says the professor is accepting PhD students."}`
- Expected shape: `{"phd_score": "high", "ra_score": "high", "confidence": "high", "reason": "Direct topical overlap plus explicit advising and RA signals."}`

### Adjacent but weaker match

- Input summary: `{"research_tags": "natural language processing; language models", "research_description": "Lab works on language understanding and reasoning.", "recent_work_cues": "Recent work is listed.", "ra_opportunity_cues": "UNKNOWN", "advising_cues": "UNKNOWN"}`
- Expected shape: `{"phd_score": "medium", "ra_score": "low-to-medium", "confidence": "medium", "reason": "NLP is adjacent but not central to the target profile, and advising / RA evidence is missing."}`

### Sparse evidence

- Input summary: `{"research_tags": "UNKNOWN", "research_description": "UNKNOWN", "recent_work_cues": "UNKNOWN", "ra_opportunity_cues": "UNKNOWN", "advising_cues": "UNKNOWN"}`
- Expected shape: `{"phd_score": "low", "ra_score": "low", "confidence": "low", "reason": "Insufficient evidence should lead to conservative scoring and explicit concerns."}`

## Ranked Results

### 1. Chen Chen 0001 (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `https://www.crcv.ucf.edu/chenchen`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in medical imaging, general AI / ML; advising cues present; RA cues present.
- phd_score: `95`
- ra_score: `95`
- rationale_phd: Explicit overlap found in: medical imaging, general AI / ML, computer vision. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: medical imaging, general AI / ML, computer vision. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: NONE
- confidence: `0.95`

### 2. Jiebo Luo 0001 (University of Rochester)

- Rank: `59`
- Department: `Department of Computer Science : University of Rochester`
- Faculty URL: `http://www.cs.rochester.edu/u/jluo`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, medical imaging; advising cues present; RA cues present.
- phd_score: `95`
- ra_score: `95`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, medical imaging, general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, medical imaging, general AI / ML. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: NONE
- confidence: `0.95`

### 3. Carl Yang 0001 (Emory University)

- Rank: `83`
- Department: `The Department of Computer Science`
- Faculty URL: `http://www.cs.emory.edu/~jyang71`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, medical imaging; advising cues present; RA cues present.
- phd_score: `95`
- ra_score: `95`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, medical imaging, general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, medical imaging, general AI / ML. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: NONE
- confidence: `0.95`

### 4. Davide Fossati (Emory University)

- Rank: `83`
- Department: `The Department of Computer Science`
- Faculty URL: `http://www.cs.emory.edu/people/faculty/individual.php?NUM=427`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues present; RA cues present.
- phd_score: `95`
- ra_score: `95`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, computer vision. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, computer vision. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: NONE
- confidence: `0.95`

### 5. Jason L. Pacheco (University of Arizona)

- Rank: `83`
- Department: `University of Arizona Department of Computer Science | Computer Science`
- Faculty URL: `https://www2.cs.arizona.edu/~pachecoj`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues present; RA cues present.
- phd_score: `95`
- ra_score: `95`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, computer vision. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, computer vision. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: NONE
- confidence: `0.95`

### 6. S. Sitharama Iyengar (Florida International University)

- Rank: `89`
- Department: `Knight Foundation School of Computing and Information Sciences`
- Faculty URL: `http://users.cis.fiu.edu/~iyengar`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, medical imaging; advising cues present; RA cues present.
- phd_score: `95`
- ra_score: `95`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, medical imaging, general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, medical imaging, general AI / ML. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: NONE
- confidence: `0.95`

### 7. Xiaohu Guo (University of Texas at Dallas)

- Rank: `55`
- Department: `UT Dallas SSO Login`
- Faculty URL: `https://www.utdallas.edu/~xxg061000`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in medical imaging, general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `95`
- ra_score: `70`
- rationale_phd: Explicit overlap found in: medical imaging, general AI / ML, computer vision. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: medical imaging, general AI / ML, computer vision. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 8. Nathan Jacobs (Washington University in St. Louis)

- Rank: `58`
- Department: `Home | WashU Computer Science & Engineering`
- Faculty URL: `https://engineering.washu.edu/faculty/Nathan-Jacobs.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in medical imaging, general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `95`
- ra_score: `70`
- rationale_phd: Explicit overlap found in: medical imaging, general AI / ML, computer vision. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: medical imaging, general AI / ML, computer vision. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 9. Junzhou Huang (University of Texas at Arlington)

- Rank: `59`
- Department: `Computer Science and Engineering - The University of Texas at Arlington`
- Faculty URL: `http://ranger.uta.edu/~huang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `95`
- ra_score: `70`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, computer vision. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, computer vision. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 10. Liang Zhao 0002 (Emory University)

- Rank: `83`
- Department: `The Department of Computer Science`
- Faculty URL: `https://cs.emory.edu/~lzhao41`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `95`
- ra_score: `70`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, computer vision. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, computer vision. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 11. Sanjay Purushotham (Univ. of Maryland - Baltimore County)

- Rank: `89`
- Department: `Department of Computer Science and Electrical Engineering – UMBC`
- Faculty URL: `https://sanjayp.is.umbc.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `95`
- ra_score: `70`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, computer vision. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, computer vision. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 12. Liang Huang 0001 (Oregon State University)

- Rank: `53`
- Department: `Electrical Engineering and Computer Science | College of Engineering`
- Faculty URL: `http://eecs.oregonstate.edu/~huanlian`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues present; RA cues present.
- phd_score: `93`
- ra_score: `95`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: NONE
- confidence: `0.95`

### 13. Da Yan 0001 (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `https://homes.luddy.indiana.edu/yanda/home.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues present; RA cues present.
- phd_score: `93`
- ra_score: `95`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: NONE
- confidence: `0.95`

### 14. Gopal Gupta 0001 (University of Texas at Dallas)

- Rank: `55`
- Department: `UT Dallas SSO Login`
- Faculty URL: `http://www.utdallas.edu/~gupta`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `93`
- ra_score: `70`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 15. Xiaozhong Liu 0001 (Worcester Polytechnic Institute)

- Rank: `75`
- Department: `Computer Science`
- Faculty URL: `https://www.wpi.edu/people/faculty/xliu14`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `93`
- ra_score: `70`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 16. Slobodan Vucetic (Temple University)

- Rank: `89`
- Department: `Department of Computer & Information Sciences | College of Science and Technology`
- Faculty URL: `http://www.dabi.temple.edu/~vucetic`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `93`
- ra_score: `70`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 17. Dejing Dou (University of Oregon)

- Rank: `97`
- Department: `Computer Science | School of Computer and Data Sciences`
- Faculty URL: `http://ix.cs.uoregon.edu/~dou`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `93`
- ra_score: `70`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 18. Taehyun Hwang (Vanderbilt University)

- Rank: `70`
- Department: `Department of Computer Science - School of EngineeringSchool of Engineering`
- Faculty URL: `https://www.hwanglab.org`
- Lab URL: `https://www.hwanglab.org`
- Source Type: `lab_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `88`
- ra_score: `75`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present. Evidence includes a lab-oriented page.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Student-mentoring cues are present. Recent activity cues are present. The evidence comes from an active lab-style page.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. Affiliation evidence relies on a lab page rather than a faculty profile.
- confidence: `0.78`

### 19. Yana Bromberg (Emory University)

- Rank: `83`
- Department: `The Department of Computer Science`
- Faculty URL: `https://bromberglab.org`
- Lab URL: `https://bromberglab.org`
- Source Type: `lab_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `88`
- ra_score: `75`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present. Evidence includes a lab-oriented page.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Student-mentoring cues are present. Recent activity cues are present. The evidence comes from an active lab-style page.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. Affiliation evidence relies on a lab page rather than a faculty profile.
- confidence: `0.78`

### 20. Lars Ruthotto (Emory University)

- Rank: `83`
- Department: `The Department of Computer Science`
- Faculty URL: `https://www.math.emory.edu/~lruthot`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in AI for science, general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `87`
- ra_score: `70`
- rationale_phd: Explicit overlap found in: AI for science, general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: AI for science, general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 21. Milos Hauskrecht (University of Pittsburgh)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `https://cs.pitt.edu/~milos`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues present; RA cues present.
- phd_score: `85`
- ra_score: `95`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: NONE
- confidence: `0.95`

### 22. Xian Fan (Florida State University)

- Rank: `67`
- Department: `DEPARTMENT OF COMPUTER SCIENCE – College of Arts and Sciences`
- Faculty URL: `https://www.cs.fsu.edu/~fan/index.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `85`
- ra_score: `70`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 23. Yingjie Lao (Tufts University)

- Rank: `70`
- Department: `Homepage | Department of Computer Science`
- Faculty URL: `https://engineering.tufts.edu/cs/people/faculty/yingjie-lao`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `85`
- ra_score: `70`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 24. Carolina Ruiz (Worcester Polytechnic Institute)

- Rank: `75`
- Department: `Computer Science`
- Faculty URL: `http://www.cs.wpi.edu/~ruiz`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `85`
- ra_score: `70`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 25. Pengcheng Shi (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `https://www.rit.edu/gccis/pengcheng-shi`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, medical imaging; advising cues present; RA cues present.
- phd_score: `83`
- ra_score: `95`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, medical imaging, general AI / ML. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, medical imaging, general AI / ML. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: NONE
- confidence: `0.83`

### 26. Stephen H. Bach (Brown University)

- Rank: `52`
- Department: `Brown University Department of Computer Science`
- Faculty URL: `https://cs.brown.edu/people/sbach`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `83`
- ra_score: `70`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, computer vision. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, computer vision. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 27. Jihun Hamm (Tulane University)

- Rank: `83`
- Department: `Computer Science | Tulane University School of Science and Engineering`
- Faculty URL: `http://www.cs.tulane.edu/~jhamm3`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in medical imaging, general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `83`
- ra_score: `70`
- rationale_phd: Explicit overlap found in: medical imaging, general AI / ML, computer vision. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: medical imaging, general AI / ML, computer vision. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 28. Gady Agam (Illinois Institute of Technology)

- Rank: `97`
- Department: `Computer Science`
- Faculty URL: `https://science.iit.edu/people/faculty/gady-agam`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in medical imaging, general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `83`
- ra_score: `70`
- rationale_phd: Explicit overlap found in: medical imaging, general AI / ML, computer vision. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: medical imaging, general AI / ML, computer vision. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 29. Cathy H. Wu (University of Delaware)

- Rank: `70`
- Department: `Computer & Information Sciences at the University of Delaware`
- Faculty URL: `http://bioinformatics.udel.edu/people/personnel/cathy_wu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `81`
- ra_score: `70`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 30. Katherine L. Bouman (California Inst. of Technology)

- Rank: `80`
- Department: `Computing + Mathematical Sciences`
- Faculty URL: `http://users.cms.caltech.edu/~klbouman`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in medical imaging, general AI / ML; advising cues UNKNOWN; RA cues present.
- phd_score: `80`
- ra_score: `85`
- rationale_phd: Explicit overlap found in: medical imaging, general AI / ML, computer vision. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: medical imaging, general AI / ML, computer vision. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.83`

### 31. Song Wang 0013 (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `https://www.cs.ucf.edu/person/songwang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `80`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, computer vision. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 32. Shihao Ji 0001 (University of Connecticut)

- Rank: `63`
- Department: `Home | School of Computing | College of Engineering`
- Faculty URL: `https://sji.soc.uconn.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `80`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, computer vision. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 33. Li Liao (University of Delaware)

- Rank: `70`
- Department: `Computer & Information Sciences at the University of Delaware`
- Faculty URL: `https://www.eecis.udel.edu/~lliao`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `80`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, computer vision. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 34. Ivelin Georgiev (Vanderbilt University)

- Rank: `70`
- Department: `Department of Computer Science - School of EngineeringSchool of Engineering`
- Faculty URL: `https://www.vanderbilt.edu/evolution/person/ivelin-georgiev`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in AI for drug discovery, computational biology / bioinformatics; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `80`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: AI for drug discovery, computational biology / bioinformatics. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: AI for drug discovery, computational biology / bioinformatics. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 35. Yaorong Ge (UNC - Charlotte)

- Rank: `75`
- Department: `Homepage - College of Computing and Informatics`
- Faculty URL: `https://cci.charlotte.edu/people/yaorong-ge`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, medical imaging; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `80`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, medical imaging, general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, medical imaging, general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 36. Jie Wei (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `https://www.ccny.cuny.edu/profiles/jie-wei`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in medical imaging, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `80`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: medical imaging, general AI / ML, computer vision. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: medical imaging, general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 37. Raviv Raich (Oregon State University)

- Rank: `53`
- Department: `Electrical Engineering and Computer Science | College of Engineering`
- Faculty URL: `http://web.engr.oregonstate.edu/~raich`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in inverse problems, general AI / ML; advising cues present; RA cues present.
- phd_score: `79`
- ra_score: `85`
- rationale_phd: Explicit overlap found in: inverse problems, general AI / ML. Research description is explicit. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: inverse problems, general AI / ML. RA or recruiting cues are explicit. Student-mentoring cues are present.
- potential_concerns: NONE
- confidence: `0.83`

### 38. Soroush Vosoughi (Dartmouth College)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `https://web.cs.dartmouth.edu/people/soroush-vosoughi`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `78`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 39. Lenore Cowen (Tufts University)

- Rank: `70`
- Department: `Homepage | Department of Computer Science`
- Faculty URL: `http://www.cs.tufts.edu/~cowen`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `78`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 40. Soha Hassoun (Tufts University)

- Rank: `70`
- Department: `Homepage | Department of Computer Science`
- Faculty URL: `http://www.cs.tufts.edu/~soha`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `78`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 41. Christian Poellabauer (Florida International University)

- Rank: `89`
- Department: `Knight Foundation School of Computing and Information Sciences`
- Faculty URL: `https://users.cs.fiu.edu/~cpoellab`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `78`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 42. Zhiyao Duan (University of Rochester)

- Rank: `59`
- Department: `Department of Computer Science : University of Rochester`
- Faculty URL: `https://hajim.rochester.edu/ece/sites/zduan`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues present; RA cues present.
- phd_score: `77`
- ra_score: `87`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision, NLP / language models. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.95`

### 43. William J. Beksi (University of Texas at Arlington)

- Rank: `59`
- Department: `Computer Science and Engineering - The University of Texas at Arlington`
- Faculty URL: `http://ranger.uta.edu/~wjbeksi`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues present; RA cues present.
- phd_score: `77`
- ra_score: `87`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision, NLP / language models. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.95`

### 44. Janardhan Rao Doppa (Washington State University)

- Rank: `86`
- Department: `School of Electrical Engineering & Computer Science`
- Faculty URL: `http://eecs.wsu.edu/~jana`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues present; RA cues present.
- phd_score: `77`
- ra_score: `87`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision, NLP / language models. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.95`

### 45. Xuyu Wang (Florida International University)

- Rank: `89`
- Department: `Knight Foundation School of Computing and Information Sciences`
- Faculty URL: `https://users.cs.fiu.edu/~xuywang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues present; RA cues present.
- phd_score: `77`
- ra_score: `87`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision, NLP / language models. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.95`

### 46. Pedro F. Felzenszwalb (Brown University)

- Rank: `52`
- Department: `Brown University Department of Computer Science`
- Faculty URL: `http://cs.brown.edu/~pff`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues present; RA cues UNKNOWN.
- phd_score: `77`
- ra_score: `62`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 47. Stefan Lee (Oregon State University)

- Rank: `53`
- Department: `Electrical Engineering and Computer Science | College of Engineering`
- Faculty URL: `http://web.engr.oregonstate.edu/~leestef`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues present; RA cues UNKNOWN.
- phd_score: `77`
- ra_score: `62`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 48. Zoran Tiganj (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `https://homes.luddy.indiana.edu/ztiganj`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues present; RA cues UNKNOWN.
- phd_score: `77`
- ra_score: `62`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 49. Chenliang Xu (University of Rochester)

- Rank: `59`
- Department: `Department of Computer Science : University of Rochester`
- Faculty URL: `https://www.cs.rochester.edu/~cxu22`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues present; RA cues UNKNOWN.
- phd_score: `77`
- ra_score: `62`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 50. M. Mondal Ananda (Florida International University)

- Rank: `89`
- Department: `Knight Foundation School of Computing and Information Sciences`
- Faculty URL: `https://www.cis.fiu.edu/faculty-staff/mondal-ananda`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `77`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Research description is explicit. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Student-mentoring cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 51. Saeed Hassanpour (Dartmouth College)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `https://www.hassanpourlab.com`
- Lab URL: `https://www.hassanpourlab.com`
- Source Type: `lab_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, medical imaging; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `75`
- ra_score: `55`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, medical imaging, general AI / ML. Research description is explicit. Evidence includes a lab-oriented page.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, medical imaging, general AI / ML. The evidence comes from an active lab-style page.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Affiliation evidence relies on a lab page rather than a faculty profile.
- confidence: `0.54`

### 52. Xinghua Shi (Temple University)

- Rank: `89`
- Department: `Department of Computer & Information Sciences | College of Science and Technology`
- Faculty URL: `https://cis.temple.edu/~mindyshi`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues present; RA cues present.
- phd_score: `73`
- ra_score: `95`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: NONE
- confidence: `0.83`

### 53. Robert McCartney (University of Connecticut)

- Rank: `63`
- Department: `Home | School of Computing | College of Engineering`
- Faculty URL: `http://www.cse.uconn.edu/people/faculty`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `73`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Student-mentoring cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.59`

### 54. Xiongye Xiao (University of Tennessee)

- Rank: `89`
- Department: `University of Tennessee`
- Faculty URL: `https://eecs.utk.edu/people/xiongye-xiao`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in AI for science, general AI / ML; advising cues UNKNOWN; RA cues present.
- phd_score: `72`
- ra_score: `85`
- rationale_phd: Explicit overlap found in: AI for science, general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: AI for science, general AI / ML. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.83`

### 55. Abhijit Mahalanobis (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `https://www.crcv.ucf.edu/person/abhijit-mahalanobis`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in medical imaging, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `72`
- ra_score: `50`
- rationale_phd: Explicit overlap found in: medical imaging, general AI / ML, computer vision. Research description is explicit.
- rationale_ra: Relevant overlap found in: medical imaging, general AI / ML, computer vision.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 56. Jinbo Bi (University of Connecticut)

- Rank: `63`
- Department: `Home | School of Computing | College of Engineering`
- Faculty URL: `http://www.engr.uconn.edu/~jinbo`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in AI for drug discovery, computational biology / bioinformatics; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `72`
- ra_score: `50`
- rationale_phd: Explicit overlap found in: AI for drug discovery, computational biology / bioinformatics, medical imaging. Research description is explicit.
- rationale_ra: Relevant overlap found in: AI for drug discovery, computational biology / bioinformatics, medical imaging.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 57. Matthias Scheutz (Tufts University)

- Rank: `70`
- Department: `Homepage | Department of Computer Science`
- Faculty URL: `http://www.cs.tufts.edu/Faculty/matthias-scheutz.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, medical imaging; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `72`
- ra_score: `50`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, medical imaging, general AI / ML. Research description is explicit.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, medical imaging, general AI / ML.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 58. Shaojie Zhang 0001 (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `http://www.cs.ucf.edu/~shzhang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues present.
- phd_score: `70`
- ra_score: `85`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.83`

### 59. Haiyan Hu (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `http://www.cs.ucf.edu/~haihu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `70`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 60. Mukul S. Bansal (University of Connecticut)

- Rank: `63`
- Department: `Home | School of Computing | College of Engineering`
- Faculty URL: `http://www.engr.uconn.edu/~mukul`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `70`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 61. Liping Liu 0001 (Tufts University)

- Rank: `70`
- Department: `Homepage | Department of Computer Science`
- Faculty URL: `https://www.eecs.tufts.edu/~liulp`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `70`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 62. David C. Wilson (UNC - Charlotte)

- Rank: `75`
- Department: `Homepage - College of Computing and Informatics`
- Faculty URL: `https://cci.charlotte.edu/people/david-wilson`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `70`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 63. Depeng Xu 0001 (UNC - Charlotte)

- Rank: `75`
- Department: `Homepage - College of Computing and Informatics`
- Faculty URL: `https://cci.charlotte.edu/people/depeng-xu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `70`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 64. Nadia Najjar (UNC - Charlotte)

- Rank: `75`
- Department: `Homepage - College of Computing and Informatics`
- Faculty URL: `https://cci.charlotte.edu/people/nadia-najjar`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `70`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 65. Eric Mazumdar (California Inst. of Technology)

- Rank: `80`
- Department: `Computing + Mathematical Sciences`
- Faculty URL: `http://users.cms.caltech.edu/~mazumdar`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `70`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 66. Mohammed J. Zaki (Rensselaer Polytechnic Institute)

- Rank: `89`
- Department: `Computer Science`
- Faculty URL: `http://www.cs.rpi.edu/~zaki`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `70`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 67. Zoran Obradovic (Temple University)

- Rank: `89`
- Department: `Department of Computer & Information Sciences | College of Science and Technology`
- Faculty URL: `http://www.dabi.temple.edu/~zoran`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `70`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 68. N. V. Vinodchandran (University of Nebraska)

- Rank: `97`
- Department: `School of Computing | Nebraska`
- Faculty URL: `http://cse.unl.edu/~vinod`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `70`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 69. Bin Ren 0002 (College of William and Mary)

- Rank: `67`
- Department: `Computer Science | School of Computing, Data Sciences & Physics | William & Mary`
- Faculty URL: `https://www.cs.wm.edu/~bren`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues present; RA cues present.
- phd_score: `69`
- ra_score: `79`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.95`

### 70. Yogesh S. Rawat (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `https://www.crcv.ucf.edu/person/rawat`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues present; RA cues UNKNOWN.
- phd_score: `69`
- ra_score: `54`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 71. Przemyslaw Musialski (NJIT)

- Rank: `63`
- Department: `Home | Department of Computer Science`
- Faculty URL: `https://web.njit.edu/~przem`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues present; RA cues UNKNOWN.
- phd_score: `69`
- ra_score: `54`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 72. Adriana Kovashka (University of Pittsburgh)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `http://people.cs.pitt.edu/~kovashka`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues present; RA cues UNKNOWN.
- phd_score: `69`
- ra_score: `54`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 73. Miguel Á. Carreira-Perpiñán (Univ. of California - Merced)

- Rank: `75`
- Department: `Computer Science & Engineering (CSE) | School of Engineering`
- Faculty URL: `https://faculty.ucmerced.edu/mcarreira-perpinan`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues present; RA cues UNKNOWN.
- phd_score: `69`
- ra_score: `54`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 74. Ming-Hsuan Yang 0001 (Univ. of California - Merced)

- Rank: `75`
- Department: `Computer Science & Engineering (CSE) | School of Engineering`
- Faculty URL: `https://faculty.ucmerced.edu/mhyang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues present; RA cues UNKNOWN.
- phd_score: `69`
- ra_score: `54`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 75. Tian Guo 0001 (Worcester Polytechnic Institute)

- Rank: `75`
- Department: `Computer Science`
- Faculty URL: `https://web.cs.wpi.edu/~tian`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues present; RA cues UNKNOWN.
- phd_score: `69`
- ra_score: `54`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 76. Matthew R. Walter (TTI Chicago)

- Rank: `89`
- Department: `TTI Chicago`
- Faculty URL: `http://ttic.uchicago.edu/~mwalter`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues present; RA cues UNKNOWN.
- phd_score: `69`
- ra_score: `54`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 77. Rui Li 0002 (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `https://www.rit.edu/directory/rxlics-rui-li`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `68`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, computer vision. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 78. Dmitry B. Goldgof (University of South Florida)

- Rank: `80`
- Department: `Bellini College of Artificial Intelligence, Cybersecurity and Computing`
- Faculty URL: `https://www.usf.edu/ai-cybersecurity-computing/people/faculty/goldgof-dmitry.aspx`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `68`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, computer vision. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 79. Michael D. Grossberg (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `https://www.ccny.cuny.edu/profiles/michael-grossberg`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in medical imaging, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `68`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: medical imaging, general AI / ML, computer vision. Recent work cues are present.
- rationale_ra: Relevant overlap found in: medical imaging, general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 80. Longin Jan Latecki (Temple University)

- Rank: `89`
- Department: `Department of Computer & Information Sciences | College of Science and Technology`
- Faculty URL: `https://cis.temple.edu/~latecki`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in medical imaging, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `68`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: medical imaging, general AI / ML, computer vision. Recent work cues are present.
- rationale_ra: Relevant overlap found in: medical imaging, general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 81. Sriram V. Pemmaraju (University of Iowa)

- Rank: `97`
- Department: `Computer Science | College of Liberal Arts and Sciences | The University of Iowa`
- Faculty URL: `https://www.cs.uiowa.edu/~sriram`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics; advising cues present; RA cues present.
- phd_score: `67`
- ra_score: `77`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: NONE
- confidence: `0.95`

### 82. Tamer Kahveci (University of Florida)

- Rank: `59`
- Department: `Department of Computer & Information Science & Engineering`
- Faculty URL: `http://www.cise.ufl.edu/~tamer`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics; advising cues present; RA cues UNKNOWN.
- phd_score: `67`
- ra_score: `52`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 83. Meikang Qiu (Augusta University)

- Rank: `97`
- Department: `School of Computer and Cyber Sciences`
- Faculty URL: `https://www.augusta.edu/faculty/directory/view.php?id=MQIU`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `66`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 84. Feng Yan 0001 (University of Houston)

- Rank: `97`
- Department: `University of Houston`
- Faculty URL: `http://www2.cs.uh.edu/~fyan`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues present; RA cues present.
- phd_score: `65`
- ra_score: `87`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision, NLP / language models. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision, NLP / language models. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.83`

### 85. Anantharaman Kalyanaraman (Washington State University)

- Rank: `86`
- Department: `School of Electrical Engineering & Computer Science`
- Faculty URL: `http://www.eecs.wsu.edu/~ananth`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues present; RA cues present.
- phd_score: `65`
- ra_score: `85`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. RA or recruiting cues are explicit. Student-mentoring cues are present.
- potential_concerns: NONE
- confidence: `0.71`

### 86. Eric L. Miller 0001 (Tufts University)

- Rank: `70`
- Department: `Homepage | Department of Computer Science`
- Faculty URL: `https://engineering.tufts.edu/cs/people/faculty/eric-miller`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in medical imaging, general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `65`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: medical imaging, general AI / ML. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: medical imaging, general AI / ML. Student-mentoring cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.59`

### 87. Lei Xie 0006 (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `http://compsci.hunter.cuny.edu/~leixie`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues present.
- phd_score: `62`
- ra_score: `75`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Research description is explicit.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. RA or recruiting cues are explicit.
- potential_concerns: No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 88. Mubarak Shah (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `https://www.crcv.ucf.edu/person/mubarak-shah`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `62`
- ra_score: `52`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 89. Niels da Vitoria Lobo (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `https://www.crcv.ucf.edu/person/niels-lobo`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `62`
- ra_score: `52`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 90. Fengchun Qiao (University of South Florida)

- Rank: `80`
- Department: `Bellini College of Artificial Intelligence, Cybersecurity and Computing`
- Faculty URL: `https://www.usf.edu/ai-cybersecurity-computing/people/faculty/fengchun_qiao.aspx`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `62`
- ra_score: `52`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 91. Sriram Chellappan (University of South Florida)

- Rank: `80`
- Department: `Bellini College of Artificial Intelligence, Cybersecurity and Computing`
- Faculty URL: `http://www.cse.usf.edu/~shri`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `62`
- ra_score: `52`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 92. Utkarsh Ojha (University of South Florida)

- Rank: `80`
- Department: `Bellini College of Artificial Intelligence, Cybersecurity and Computing`
- Faculty URL: `https://www.usf.edu/ai-cybersecurity-computing/people/faculty/utkarsh_ojha.aspx`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `62`
- ra_score: `52`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 93. Fengguang Song (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `https://engineering.indiana.edu/contact/profile/index.html?Fengguang_Song`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `62`
- ra_score: `50`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Research description is explicit.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 94. Chris Bailey-Kellogg (Dartmouth College)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `http://www.cs.dartmouth.edu/~cbk`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `62`
- ra_score: `50`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Research description is explicit.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 95. Ioannis Koutis (NJIT)

- Rank: `63`
- Department: `Home | Department of Computer Science`
- Faculty URL: `https://web.njit.edu/~ikoutis`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `62`
- ra_score: `50`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Research description is explicit.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 96. Xiao Fu 0001 (Oregon State University)

- Rank: `53`
- Department: `Electrical Engineering and Computer Science | College of Engineering`
- Faculty URL: `http://people.oregonstate.edu/~fuxia`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues present.
- phd_score: `61`
- ra_score: `71`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.95`

### 97. Qiben Yan (Michigan State University)

- Rank: `67`
- Department: `Computer Science and Engineering | College of Engineering`
- Faculty URL: `https://cse.msu.edu/~qyan`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues present.
- phd_score: `61`
- ra_score: `71`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.95`

### 98. Ilya Safro (University of Delaware)

- Rank: `70`
- Department: `Computer & Information Sciences at the University of Delaware`
- Faculty URL: `https://www.eecis.udel.edu/~isafro`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues present.
- phd_score: `61`
- ra_score: `71`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.95`

### 99. Abolfazl Razi (Clemson University)

- Rank: `75`
- Department: `School of Computing`
- Faculty URL: `https://arazi.people.clemson.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues present.
- phd_score: `61`
- ra_score: `71`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.95`

### 100. Long Cheng 0005 (Clemson University)

- Rank: `75`
- Department: `School of Computing`
- Faculty URL: `https://people.computing.clemson.edu/~lcheng2`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues present.
- phd_score: `61`
- ra_score: `71`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.95`

### 101. Kai Shu (Emory University)

- Rank: `83`
- Department: `The Department of Computer Science`
- Faculty URL: `https://www.cs.emory.edu/~kshu5`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues present.
- phd_score: `61`
- ra_score: `71`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.95`

### 102. Thien Huu Nguyen (University of Oregon)

- Rank: `97`
- Department: `Computer Science | School of Computer and Data Sciences`
- Faculty URL: `http://ix.cs.uoregon.edu/~thien`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues present.
- phd_score: `61`
- ra_score: `71`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.95`

### 103. Filippo Menczer (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `http://cnets.indiana.edu/fil`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues UNKNOWN.
- phd_score: `61`
- ra_score: `46`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 104. Prateek Sharma (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `http://homes.sice.indiana.edu/prateeks`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues UNKNOWN.
- phd_score: `61`
- ra_score: `46`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 105. Pengfei Li (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `https://people.rit.edu/pflics`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues UNKNOWN.
- phd_score: `61`
- ra_score: `46`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 106. Jiaxin Huang 0001 (Washington University in St. Louis)

- Rank: `58`
- Department: `Home | WashU Computer Science & Engineering`
- Faculty URL: `https://engineering.washu.edu/faculty/Jiaxin-Huang.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues UNKNOWN.
- phd_score: `61`
- ra_score: `46`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 107. Daisy Zhe Wang (University of Florida)

- Rank: `59`
- Department: `Department of Computer & Information Science & Engineering`
- Faculty URL: `http://dsr.cise.ufl.edu/daisyw`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues UNKNOWN.
- phd_score: `61`
- ra_score: `46`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 108. Andrew T. Campbell (Dartmouth College)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `https://www.cs.dartmouth.edu/~campbell`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues UNKNOWN.
- phd_score: `61`
- ra_score: `46`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 109. Yi He 0007 (College of William and Mary)

- Rank: `67`
- Department: `Computer Science | School of Computing, Data Sciences & Physics | William & Mary`
- Faculty URL: `https://yhe15.people.wm.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues UNKNOWN.
- phd_score: `61`
- ra_score: `46`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 110. Kyumin Lee (Worcester Polytechnic Institute)

- Rank: `75`
- Department: `Computer Science`
- Faculty URL: `http://web.cs.wpi.edu/~kmlee`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues UNKNOWN.
- phd_score: `61`
- ra_score: `46`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 111. Mo Sha 0001 (Florida International University)

- Rank: `89`
- Department: `Knight Foundation School of Computing and Information Sciences`
- Faculty URL: `https://users.cs.fiu.edu/~msha`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues UNKNOWN.
- phd_score: `61`
- ra_score: `46`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 112. Wenbin Zhang 0002 (Florida International University)

- Rank: `89`
- Department: `Knight Foundation School of Computing and Information Sciences`
- Faculty URL: `https://users.cs.fiu.edu/~wbzhang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues UNKNOWN.
- phd_score: `61`
- ra_score: `46`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 113. Shimei Pan (Univ. of Maryland - Baltimore County)

- Rank: `89`
- Department: `Department of Computer Science and Electrical Engineering – UMBC`
- Faculty URL: `https://nlp-lab.umbc.edu/home/shimei`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues UNKNOWN.
- phd_score: `61`
- ra_score: `46`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 114. Austin J. Brockmeier (University of Delaware)

- Rank: `70`
- Department: `Computer & Information Sciences at the University of Delaware`
- Faculty URL: `https://www.cis.udel.edu/people/faculty-profile/?id=264`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `60`
- ra_score: `50`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, computer vision.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, computer vision.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 115. Ioannis M. Rekleitis (University of Delaware)

- Rank: `70`
- Department: `Computer & Information Sciences at the University of Delaware`
- Faculty URL: `https://www.cis.udel.edu/people/faculty/ioannis-rekleitis`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `60`
- ra_score: `50`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, computer vision.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, computer vision.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 116. Rahmatollah Beheshti (University of Delaware)

- Rank: `70`
- Department: `Computer & Information Sciences at the University of Delaware`
- Faculty URL: `https://www.cis.udel.edu/people/faculty-profile/?id=265`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `60`
- ra_score: `50`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, computer vision.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, computer vision.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 117. Roghayeh Barmaki (University of Delaware)

- Rank: `70`
- Department: `Computer & Information Sciences at the University of Delaware`
- Faculty URL: `https://www.cis.udel.edu/people/faculty-profile/?id=263`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `60`
- ra_score: `50`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML, computer vision.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML, computer vision.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 118. Michael A. Gennert (Worcester Polytechnic Institute)

- Rank: `75`
- Department: `Computer Science`
- Faculty URL: `http://www.wpi.edu/~michaelg`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in medical imaging, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `60`
- ra_score: `50`
- rationale_phd: Explicit overlap found in: medical imaging, general AI / ML, computer vision.
- rationale_ra: Relevant overlap found in: medical imaging, general AI / ML, computer vision.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 119. Robert Pless (George Washington University)

- Rank: `97`
- Department: `Department of Computer Science | School of Engineering & Applied Science | The George Washington University`
- Faculty URL: `https://www.cs.seas.gwu.edu/robert-pless`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in medical imaging, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `60`
- ra_score: `50`
- rationale_phd: Explicit overlap found in: medical imaging, general AI / ML, computer vision.
- rationale_ra: Relevant overlap found in: medical imaging, general AI / ML, computer vision.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 120. Carola Wenk (Tulane University)

- Rank: `83`
- Department: `Computer Science | Tulane University School of Science and Engineering`
- Faculty URL: `http://www.cs.tulane.edu/~carola`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics; advising cues present; RA cues UNKNOWN.
- phd_score: `59`
- ra_score: `42`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics. Research description is explicit. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics. Student-mentoring cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.59`

### 121. Rebecca A. Hutchinson (Oregon State University)

- Rank: `53`
- Department: `Electrical Engineering and Computer Science | College of Engineering`
- Faculty URL: `http://web.engr.oregonstate.edu/~rah`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `58`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 122. Saúl A. Blanco (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `https://luddy.indiana.edu/contact/profile/?Saul_Blanco`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `58`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 123. Xuhong Zhang 0001 (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `https://luddy.indiana.edu/contact/profile/?Xuhong_Zhang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `58`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 124. Sanjay Ranka (University of Florida)

- Rank: `59`
- Department: `Department of Computer & Information Science & Engineering`
- Faculty URL: `https://www.cise.ufl.edu/people/faculty/ranka`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `58`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 125. Daniel Stefankovic (University of Rochester)

- Rank: `59`
- Department: `Department of Computer Science : University of Rochester`
- Faculty URL: `https://www.cs.rochester.edu/~stefanko`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `58`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 126. Ralf M. Häfner (University of Rochester)

- Rank: `59`
- Department: `Department of Computer Science : University of Rochester`
- Faculty URL: `https://www2.bcs.rochester.edu/sites/haefnerlab/index.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `58`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 127. Omer Tamuz (California Inst. of Technology)

- Rank: `80`
- Department: `Computing + Mathematical Sciences`
- Faculty URL: `http://tamuz.caltech.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `58`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 128. Bryan David Minor (Washington State University)

- Rank: `86`
- Department: `School of Electrical Engineering & Computer Science`
- Faculty URL: `https://school.eecs.wsu.edu/people/faculty/bryan-minor`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `58`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 129. Dae Hyun Kim 0004 (Washington State University)

- Rank: `86`
- Department: `School of Electrical Engineering & Computer Science`
- Faculty URL: `https://school.eecs.wsu.edu/people/faculty/dae-hyun-kim`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `58`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 130. Trong Nghia Hoang (Washington State University)

- Rank: `86`
- Department: `School of Electrical Engineering & Computer Science`
- Faculty URL: `https://school.eecs.wsu.edu/faculty/profile/?nid=trongnghia.hoang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `58`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 131. Giri Narasimhan (Florida International University)

- Rank: `89`
- Department: `Knight Foundation School of Computing and Information Sciences`
- Faculty URL: `http://www.cs.fiu.edu/~giri`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `58`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 132. Asa Ben-Hur (Colorado State University)

- Rank: `97`
- Department: `Department of Computer Science | CSU – Department of Computer Science at Colorado State University`
- Faculty URL: `http://www.cs.colostate.edu/~asa`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `58`
- ra_score: `60`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 133. Xumin Liu (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `https://www.cs.rit.edu/people/faculty/xl`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues present; RA cues present.
- phd_score: `57`
- ra_score: `79`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.83`

### 134. Catie Chang (Vanderbilt University)

- Rank: `70`
- Department: `Department of Computer Science - School of EngineeringSchool of Engineering`
- Faculty URL: `http://www.cchanglab.net`
- Lab URL: `http://www.cchanglab.net`
- Source Type: `lab_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues present.
- phd_score: `56`
- ra_score: `68`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present. Evidence includes a lab-oriented page.
- rationale_ra: Relevant overlap found in: general AI / ML. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present. The evidence comes from an active lab-style page.
- potential_concerns: No explicit evidence of the user's highest-priority domains. Affiliation evidence relies on a lab page rather than a faculty profile.
- confidence: `0.90`

### 135. Chia-Ling Tsai (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `https://www.cs.qc.cuny.edu/tsai.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `56`
- ra_score: `58`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, computer vision. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, computer vision. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 136. Adriana Schulz (Brown University)

- Rank: `52`
- Department: `Brown University Department of Computer Science`
- Faculty URL: `https://www.computationaldesign.group/adriana`
- Lab URL: `https://www.computationaldesign.group/adriana`
- Source Type: `lab_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `56`
- ra_score: `43`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present. Evidence includes a lab-oriented page.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present. The evidence comes from an active lab-style page.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. Affiliation evidence relies on a lab page rather than a faculty profile.
- confidence: `0.78`

### 137. Tijana Milenkovic (University of Notre Dame)

- Rank: `59`
- Department: `Home - Computer Science and Engineering`
- Faculty URL: `http://www3.nd.edu/~tmilenko`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics; advising cues present; RA cues UNKNOWN.
- phd_score: `55`
- ra_score: `52`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 138. Ting-Zhu Huang (Univ. of Maryland - Baltimore County)

- Rank: `89`
- Department: `Department of Computer Science and Electrical Engineering – UMBC`
- Faculty URL: `http://www.csee.umbc.edu/~zt`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics; advising cues present; RA cues UNKNOWN.
- phd_score: `55`
- ra_score: `52`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 139. Liqiang Wang 0001 (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `http://www.cs.ucf.edu/~lwang/index.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues present.
- phd_score: `54`
- ra_score: `69`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.83`

### 140. Ali Shokoufandeh (Drexel University)

- Rank: `89`
- Department: `Computer Science Department | Drexel CCI`
- Faculty URL: `http://drexel.edu/cci/contact/Faculty/Shokoufandeh-Ali`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues present.
- phd_score: `54`
- ra_score: `69`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.83`

### 141. Srinath Sridhar 0002 (Brown University)

- Rank: `52`
- Department: `Brown University Department of Computer Science`
- Faculty URL: `https://cs.brown.edu/people/ssrinath`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `54`
- ra_score: `44`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 142. Haim Schweitzer (University of Texas at Dallas)

- Rank: `55`
- Department: `UT Dallas SSO Login`
- Faculty URL: `http://www.utdallas.edu/~haim`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `54`
- ra_score: `44`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 143. Bartosz Krawczyk (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `https://www.rit.edu/directory/bxkcis-bartosz-krawczyk`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `54`
- ra_score: `44`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 144. Cong Shi 0004 (NJIT)

- Rank: `63`
- Department: `Home | Department of Computer Science`
- Faculty URL: `https://web.njit.edu/~cs638`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `54`
- ra_score: `44`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 145. Anil K. Jain 0001 (Michigan State University)

- Rank: `67`
- Department: `Computer Science and Engineering | College of Engineering`
- Faculty URL: `https://www.cse.msu.edu/~jain`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `54`
- ra_score: `44`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 146. Karthik Nandakumar (Michigan State University)

- Rank: `67`
- Department: `Computer Science and Engineering | College of Engineering`
- Faculty URL: `https://www.cse.msu.edu/~nandakum`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `54`
- ra_score: `44`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 147. Adnan Siraj Rakin (Binghamton University)

- Rank: `70`
- Department: `School of Computing`
- Faculty URL: `https://www.binghamton.edu/computer-science/people/profile.html?id=arakin`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `54`
- ra_score: `44`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 148. Shawn D. Newsam (Univ. of California - Merced)

- Rank: `75`
- Department: `Computer Science & Engineering (CSE) | School of Engineering`
- Faculty URL: `https://faculty.ucmerced.edu/snewsam/index.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `54`
- ra_score: `44`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 149. Yu Sun 0004 (University of South Florida)

- Rank: `80`
- Department: `Bellini College of Artificial Intelligence, Cybersecurity and Computing`
- Faculty URL: `http://www.cse.usf.edu/~yusun`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `54`
- ra_score: `44`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 150. Zhengming Ding (Tulane University)

- Rank: `83`
- Department: `Computer Science | Tulane University School of Science and Engineering`
- Faculty URL: `https://sse.tulane.edu/cs/faculty/Ding`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `54`
- ra_score: `44`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 151. Sos S. Agaian (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `https://www.csi.cuny.edu/campus-directory/sos-agaian`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `54`
- ra_score: `44`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 152. Richard Souvenir (Temple University)

- Rank: `89`
- Department: `Department of Computer & Information Sciences | College of Science and Technology`
- Faculty URL: `https://cis.temple.edu/~souvenir`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `54`
- ra_score: `44`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 153. Mohamed Akrout (University of Tennessee)

- Rank: `89`
- Department: `University of Tennessee`
- Faculty URL: `https://eecs.utk.edu/people/mohamed-akrout`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in inverse problems; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `54`
- ra_score: `44`
- rationale_phd: Explicit overlap found in: inverse problems. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: inverse problems. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 154. James B. D. Joshi (University of Pittsburgh)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `http://www.sis.pitt.edu/jjoshi`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues present.
- phd_score: `53`
- ra_score: `63`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.95`

### 155. Jian Liu 0001 (University of Georgia)

- Rank: `75`
- Department: `University of Georgia`
- Faculty URL: `https://www.cs.uga.edu/news/stories/2025/2025-summer-update-director-school-computing`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues present.
- phd_score: `53`
- ra_score: `63`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.95`

### 156. Sanda M. Harabagiu (University of Texas at Dallas)

- Rank: `55`
- Department: `UT Dallas SSO Login`
- Faculty URL: `http://www.utdallas.edu/~sanda`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues present.
- phd_score: `53`
- ra_score: `61`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. RA or recruiting cues are explicit. Student-mentoring cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.83`

### 157. Margaret M. Burnett (Oregon State University)

- Rank: `53`
- Department: `Electrical Engineering and Computer Science | College of Engineering`
- Faculty URL: `http://eecs.oregonstate.edu/~burnett`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `53`
- ra_score: `38`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 158. Richard Zanibbi (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `https://www.cs.rit.edu/~rlaz`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `53`
- ra_score: `38`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 159. Gregory Kehne (Washington University in St. Louis)

- Rank: `58`
- Department: `Home | WashU Computer Science & Engineering`
- Faculty URL: `https://engineering.washu.edu/faculty/Gregory-Kehne.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `53`
- ra_score: `38`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 160. Alin Dobra (University of Florida)

- Rank: `59`
- Department: `Department of Computer & Information Science & Engineering`
- Faculty URL: `http://www.cise.ufl.edu/~adobra`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `53`
- ra_score: `38`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 161. Kevin R. B. Butler (University of Florida)

- Rank: `59`
- Department: `Department of Computer & Information Science & Engineering`
- Faculty URL: `http://cise.ufl.edu/~butler`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `53`
- ra_score: `38`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 162. Jing Li 0025 (NJIT)

- Rank: `63`
- Department: `Home | Department of Computer Science`
- Faculty URL: `https://web.njit.edu/~jingli`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `53`
- ra_score: `38`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 163. Qun Li 0001 (College of William and Mary)

- Rank: `67`
- Department: `Computer Science | School of Computing, Data Sciences & Physics | William & Mary`
- Faculty URL: `http://www.cs.wm.edu/~liqun`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `53`
- ra_score: `38`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 164. Daniel L. Chester (University of Delaware)

- Rank: `70`
- Department: `Computer & Information Sciences at the University of Delaware`
- Faculty URL: `https://www.eecis.udel.edu/~chester`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `53`
- ra_score: `38`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 165. Dong Li 0001 (Univ. of California - Merced)

- Rank: `75`
- Department: `Computer Science & Engineering (CSE) | School of Engineering`
- Faculty URL: `https://faculty.ucmerced.edu/dong-li`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `53`
- ra_score: `38`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 166. Ana L. Milanova (Rensselaer Polytechnic Institute)

- Rank: `89`
- Department: `Computer Science`
- Faculty URL: `http://www.cs.rpi.edu/~milanova`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `53`
- ra_score: `38`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 167. H. Howie Huang (George Washington University)

- Rank: `97`
- Department: `Department of Computer Science | School of Engineering & Applied Science | The George Washington University`
- Faculty URL: `https://www2.seas.gwu.edu/~howie`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `53`
- ra_score: `38`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 168. Steven Bethard (University of Arizona)

- Rank: `83`
- Department: `University of Arizona Department of Computer Science | Computer Science`
- Faculty URL: `http://bethard.faculty.arizona.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues UNKNOWN.
- phd_score: `53`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Student-mentoring cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 169. Cynthia Matuszek (Univ. of Maryland - Baltimore County)

- Rank: `89`
- Department: `Department of Computer Science and Electrical Engineering – UMBC`
- Faculty URL: `http://www.csee.umbc.edu/~cmat`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues UNKNOWN.
- phd_score: `53`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Student-mentoring cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 170. Jian Xiang (UNC - Charlotte)

- Rank: `75`
- Department: `Homepage - College of Computing and Informatics`
- Faculty URL: `https://cci.charlotte.edu/people/jian-xiang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `52`
- ra_score: `42`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 171. Mirsad Hadzikadic (UNC - Charlotte)

- Rank: `75`
- Department: `Homepage - College of Computing and Informatics`
- Faculty URL: `https://cci.charlotte.edu/people/mirsad-hadzikadic`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `52`
- ra_score: `42`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 172. Weichao Wang (UNC - Charlotte)

- Rank: `75`
- Department: `Homepage - College of Computing and Informatics`
- Faculty URL: `https://cci.charlotte.edu/people/weichao-wang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `52`
- ra_score: `42`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 173. Aaron F. Bobick (Washington University in St. Louis)

- Rank: `58`
- Department: `Home | WashU Computer Science & Engineering`
- Faculty URL: `https://engineering.washu.edu/faculty/Aaron-Bobick.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computer vision; advising cues present; RA cues UNKNOWN.
- phd_score: `51`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: computer vision. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computer vision. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.83`

### 174. Qi Yu 0001 (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `https://www.rit.edu/mining/qi-yu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues present.
- phd_score: `50`
- ra_score: `77`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision, NLP / language models. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 175. Kejun Huang (University of Florida)

- Rank: `59`
- Department: `Department of Computer & Information Science & Engineering`
- Faculty URL: `https://cise.ufl.edu/~kejun`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `50`
- ra_score: `52`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 176. Feng Liu 0037 (Drexel University)

- Rank: `89`
- Department: `Computer Science Department | Drexel CCI`
- Faculty URL: `https://drexel.edu/cci/about/directory/L/Liu-Feng`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `50`
- ra_score: `52`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 177. Jason Tsong-Li Wang (NJIT)

- Rank: `63`
- Department: `Home | Department of Computer Science`
- Faculty URL: `https://web.njit.edu/~wangj`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `50`
- ra_score: `50`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 178. Pavel Skums (University of Connecticut)

- Rank: `63`
- Department: `Home | School of Computing | College of Engineering`
- Faculty URL: `https://engineering.uconn.edu/person/pavel-skums`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `50`
- ra_score: `50`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 179. Hongyang Gao (Iowa State University)

- Rank: `80`
- Department: `Department of Computer Science`
- Faculty URL: `https://faculty.sites.iastate.edu/hygao`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `50`
- ra_score: `50`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 180. Zhaohui S. Qin (Emory University)

- Rank: `83`
- Department: `The Department of Computer Science`
- Faculty URL: `https://www.sph.emory.edu/faculty/profile/index.php?FID=8697`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `50`
- ra_score: `50`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 181. Lawrence B. Holder (Washington State University)

- Rank: `86`
- Department: `School of Electrical Engineering & Computer Science`
- Faculty URL: `http://www.eecs.wsu.edu/~holder`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics, general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `50`
- ra_score: `50`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics, general AI / ML.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics, general AI / ML.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 182. Amrit Singh Bedi (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `https://www.cecs.ucf.edu/faculty/21197`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues present.
- phd_score: `49`
- ra_score: `71`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.83`

### 183. Brian D. Davison 0001 (Lehigh University)

- Rank: `97`
- Department: `Computer Science & Engineering | P.C. Rossin College of Engineering & Applied Science`
- Faculty URL: `http://www.cse.lehigh.edu/~brian`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues present.
- phd_score: `49`
- ra_score: `71`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.83`

### 184. Weijie Zhao 0001 (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `https://www.cs.rit.edu/~wjz`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues UNKNOWN.
- phd_score: `49`
- ra_score: `46`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 185. Fuhai Li 0001 (Washington University in St. Louis)

- Rank: `58`
- Department: `Home | WashU Computer Science & Engineering`
- Faculty URL: `https://engineering.washu.edu/faculty/Fuhai-Li.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues UNKNOWN.
- phd_score: `49`
- ra_score: `46`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 186. Yixin Chen 0001 (Washington University in St. Louis)

- Rank: `58`
- Department: `Home | WashU Computer Science & Engineering`
- Faculty URL: `https://engineering.washu.edu/faculty/Yixin-Chen.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues UNKNOWN.
- phd_score: `49`
- ra_score: `46`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 187. Wan Du (Univ. of California - Merced)

- Rank: `75`
- Department: `Computer Science & Engineering (CSE) | School of Engineering`
- Faculty URL: `https://faculty.ucmerced.edu/wdu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues present; RA cues UNKNOWN.
- phd_score: `49`
- ra_score: `46`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 188. Sinisa Todorovic (Oregon State University)

- Rank: `53`
- Department: `Electrical Engineering and Computer Science | College of Engineering`
- Faculty URL: `http://web.engr.oregonstate.edu/~sinisa`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues present; RA cues UNKNOWN.
- phd_score: `49`
- ra_score: `44`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Student-mentoring cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.59`

### 189. Soneya Binta Hossain (University of Texas at Dallas)

- Rank: `55`
- Department: `UT Dallas SSO Login`
- Faculty URL: `https://assert-lab.github.io`
- Lab URL: `https://assert-lab.github.io`
- Source Type: `lab_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `49`
- ra_score: `41`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present. Evidence includes a lab-oriented page.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present. The evidence comes from an active lab-style page.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Affiliation evidence relies on a lab page rather than a faculty profile.
- confidence: `0.66`

### 190. Sudeep Sarkar (University of South Florida)

- Rank: `80`
- Department: `Bellini College of Artificial Intelligence, Cybersecurity and Computing`
- Faculty URL: `http://www.cse.usf.edu/~sarkar`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in medical imaging, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `48`
- ra_score: `48`
- rationale_phd: Explicit overlap found in: medical imaging, computer vision.
- rationale_ra: Relevant overlap found in: medical imaging, computer vision.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 191. Kevin Liu (Michigan State University)

- Rank: `67`
- Department: `Computer Science and Engineering | College of Engineering`
- Faculty URL: `http://www.cse.msu.edu/~kjl`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics; advising cues present; RA cues UNKNOWN.
- phd_score: `47`
- ra_score: `42`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics. Student-mentoring cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.59`

### 192. David Mohaisen (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `http://cs.ucf.edu/~mohaisen`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues present.
- phd_score: `46`
- ra_score: `61`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.83`

### 193. Lenhart K. Schubert (University of Rochester)

- Rank: `59`
- Department: `Department of Computer Science : University of Rochester`
- Faculty URL: `https://www.cs.rochester.edu/~schubert`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues present.
- phd_score: `46`
- ra_score: `61`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.83`

### 194. Senjuti Basu Roy (NJIT)

- Rank: `63`
- Department: `Home | Department of Computer Science`
- Faculty URL: `https://web.njit.edu/~senjutib`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues present.
- phd_score: `46`
- ra_score: `61`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.83`

### 195. Parisa Kordjamshidi (Michigan State University)

- Rank: `67`
- Department: `Computer Science and Engineering | College of Engineering`
- Faculty URL: `https://www.cse.msu.edu/~kordjams`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues present.
- phd_score: `46`
- ra_score: `61`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.83`

### 196. Bashima Islam (Worcester Polytechnic Institute)

- Rank: `75`
- Department: `Computer Science`
- Faculty URL: `https://users.wpi.edu/~bislam`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues present.
- phd_score: `46`
- ra_score: `61`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.83`

### 197. Lizhong Chen (Oregon State University)

- Rank: `53`
- Department: `Electrical Engineering and Computer Science | College of Engineering`
- Faculty URL: `http://web.engr.oregonstate.edu/~chenliz`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 198. Jessica Ouyang 0001 (University of Texas at Dallas)

- Rank: `55`
- Department: `UT Dallas SSO Login`
- Faculty URL: `https://personal.utdallas.edu/~jessica.ouyang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 199. Sriraam Natarajan (University of Texas at Dallas)

- Rank: `55`
- Department: `UT Dallas SSO Login`
- Faculty URL: `http://utdallas.edu/~sxn177430`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 200. Ashiqur R. KhudaBukhsh (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `https://www.rit.edu/directory/axkvse-ashique-khudabukhsh`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 201. Roshan Lalintha Peiris (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `https://www.rit.edu/directory/rxpics-roshan-peiris`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 202. Yiqin Zhao (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `https://www.rit.edu/directory/yzigm-yiqin-zhao`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 203. David Chiang 0001 (University of Notre Dame)

- Rank: `59`
- Department: `Home - Computer Science and Engineering`
- Faculty URL: `http://www3.nd.edu/~dchiang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 204. Yanfang Ye 0001 (University of Notre Dame)

- Rank: `59`
- Department: `Home - Computer Science and Engineering`
- Faculty URL: `https://engineering.nd.edu/faculty/yanfang-fanny-ye`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 205. James F. Allen (University of Rochester)

- Rank: `59`
- Department: `Department of Computer Science : University of Rochester`
- Faculty URL: `http://www.cs.rochester.edu/~james`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 206. Sarah Masud Preum (Dartmouth College)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `https://web.cs.dartmouth.edu/people/sarah-masud-preum`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 207. Daqing He (University of Pittsburgh)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `http://www.pitt.edu/~dah44`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 208. Diane J. Litman (University of Pittsburgh)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `https://www.cs.pitt.edu/~litman`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 209. Guanhua Yan (Binghamton University)

- Rank: `70`
- Department: `School of Computing`
- Faculty URL: `https://www.binghamton.edu/cs/people/ghyan.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 210. Zhaohan Xi (Binghamton University)

- Rank: `70`
- Department: `School of Computing`
- Faculty URL: `https://www.binghamton.edu/computer-science/people/profile.html?id=zxi1`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 211. Chunsheng Xin (Iowa State University)

- Rank: `80`
- Department: `Department of Computer Science`
- Faculty URL: `https://www.cs.iastate.edu/people/sam-xin`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 212. Gene Louis Kim (University of South Florida)

- Rank: `80`
- Department: `Bellini College of Artificial Intelligence, Cybersecurity and Computing`
- Faculty URL: `https://cse.usf.edu/~genekim`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 213. Eugene Agichtein (Emory University)

- Rank: `83`
- Department: `The Department of Computer Science`
- Faculty URL: `https://cs.emory.edu/~eugene`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 214. Fei Liu 0004 (Emory University)

- Rank: `83`
- Department: `The Department of Computer Science`
- Faculty URL: `https://www.cs.emory.edu/~fliu40`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 215. Jinho D. Choi (Emory University)

- Rank: `83`
- Department: `The Department of Computer Science`
- Faculty URL: `https://cs.emory.edu/~choi/home.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 216. Aron Culotta (Tulane University)

- Rank: `83`
- Department: `Computer Science | Tulane University School of Science and Engineering`
- Faculty URL: `http://www.cs.tulane.edu/~aculotta`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 217. Saad Hassan (Tulane University)

- Rank: `83`
- Department: `Computer Science | Tulane University School of Science and Engineering`
- Faculty URL: `https://sse.tulane.edu/cs/faculty/hassan`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 218. Sandiway Fong (University of Arizona)

- Rank: `83`
- Department: `University of Arizona Department of Computer Science | Computer Science`
- Faculty URL: `http://elmo.sbs.arizona.edu/sandiway`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 219. Mark A. Finlayson (Florida International University)

- Rank: `89`
- Department: `Knight Foundation School of Computing and Information Sciences`
- Faculty URL: `http://cs.fiu.edu/~markaf`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 220. Jianxi Gao (Rensselaer Polytechnic Institute)

- Rank: `89`
- Department: `Computer Science`
- Faculty URL: `https://faculty.rpi.edu/jianxi-gao`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 221. Stacy Patterson (Rensselaer Polytechnic Institute)

- Rank: `89`
- Department: `Computer Science`
- Faculty URL: `http://www.cs.rpi.edu/~pattes3`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 222. Eduard C. Dragut (Temple University)

- Rank: `89`
- Department: `Department of Computer & Information Sciences | College of Science and Technology`
- Faculty URL: `https://cis.temple.edu/~edragut`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 223. Francis Ferraro (Univ. of Maryland - Baltimore County)

- Rank: `89`
- Department: `Department of Computer Science and Electrical Engineering – UMBC`
- Faculty URL: `https://www.csee.umbc.edu/~ferraro`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 224. Fnu Suya (University of Tennessee)

- Rank: `89`
- Department: `University of Tennessee`
- Faculty URL: `https://eecs.utk.edu/people/fnu-suya`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 225. Arjun Mukherjee (University of Houston)

- Rank: `97`
- Department: `University of Houston`
- Faculty URL: `http://www2.cs.uh.edu/~arjun`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 226. Muchao Ye (University of Iowa)

- Rank: `97`
- Department: `Computer Science | College of Liberal Arts and Sciences | The University of Iowa`
- Faculty URL: `https://cs.uiowa.edu/people/muchao-ye`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 227. Hau Chan (University of Nebraska)

- Rank: `97`
- Department: `School of Computing | Nebraska`
- Faculty URL: `https://cse.unl.edu/~hchan`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 228. Alan Fern (Oregon State University)

- Rank: `53`
- Department: `Electrical Engineering and Computer Science | College of Engineering`
- Faculty URL: `http://eecs.oregonstate.edu/~afern`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `34`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 229. Gita Reese Sukthankar (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `http://www.eecs.ucf.edu/~gitars`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `34`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 230. Hassan Foroosh (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `http://www.cs.ucf.edu/~foroosh`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `34`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 231. Arun Ross (Michigan State University)

- Rank: `67`
- Department: `Computer Science and Engineering | College of Engineering`
- Faculty URL: `http://www.cse.msu.edu/~rossarun`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `34`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 232. Charles V. Stewart (Rensselaer Polytechnic Institute)

- Rank: `89`
- Department: `Computer Science`
- Faculty URL: `http://www.cs.rpi.edu/~stewart`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `34`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 233. Hairong Qi 0001 (University of Tennessee)

- Rank: `89`
- Department: `University of Tennessee`
- Faculty URL: `https://eecs.utk.edu/people/hairong-qi`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `34`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 234. Bruce A. Draper (Colorado State University)

- Rank: `97`
- Department: `Department of Computer Science | CSU – Department of Computer Science at Colorado State University`
- Faculty URL: `http://www.cs.colostate.edu/~draper`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `46`
- ra_score: `34`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 235. Ulugbek Kamilov (Washington University in St. Louis)

- Rank: `58`
- Department: `Home | WashU Computer Science & Engineering`
- Faculty URL: `https://cigroup.wustl.edu`
- Lab URL: `https://cigroup.wustl.edu`
- Source Type: `lab_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `45`
- ra_score: `49`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Recent work cues are present. Evidence includes a lab-oriented page.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Recent activity cues are present. The evidence comes from an active lab-style page.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Affiliation evidence relies on a lab page rather than a faculty profile.
- confidence: `0.54`

### 236. Xiaowei Jia (University of Pittsburgh)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `https://sites.pitt.edu/~xiaowei`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `45`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 237. Hari Sundar (Tufts University)

- Rank: `70`
- Department: `Homepage | Department of Computer Science`
- Faculty URL: `https://engineering.tufts.edu/cs/people/faculty/hari-sundar`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `45`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 238. James M. Murphy (Tufts University)

- Rank: `70`
- Department: `Homepage | Department of Computer Science`
- Faculty URL: `https://engineering.tufts.edu/cs/people/faculty/james-murphy`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `45`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 239. Josephine Wolff (Tufts University)

- Rank: `70`
- Department: `Homepage | Department of Computer Science`
- Faculty URL: `https://engineering.tufts.edu/cs/people/faculty/josephine-wolff`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `45`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 240. Jack H. Noble (Vanderbilt University)

- Rank: `70`
- Department: `Department of Computer Science - School of EngineeringSchool of Engineering`
- Faculty URL: `https://my.vanderbilt.edu/jacknoble`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `45`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 241. Christopher D. Carothers (Rensselaer Polytechnic Institute)

- Rank: `89`
- Department: `Computer Science`
- Faculty URL: `http://www.cs.rpi.edu/~chrisc`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `45`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 242. Brian Y. Chen (Lehigh University)

- Rank: `97`
- Department: `Computer Science & Engineering | P.C. Rossin College of Engineering & Applied Science`
- Faculty URL: `http://www.cse.lehigh.edu/~chen`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics; advising cues UNKNOWN; RA cues present.
- phd_score: `44`
- ra_score: `57`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics. Research description is explicit.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics. RA or recruiting cues are explicit.
- potential_concerns: No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 243. Qian Yang (University of Connecticut)

- Rank: `63`
- Department: `Home | School of Computing | College of Engineering`
- Faculty URL: `https://www.qianyanglab.com`
- Lab URL: `https://www.qianyanglab.com`
- Source Type: `lab_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `44`
- ra_score: `43`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present. Advising or prospective-student cues are present. Evidence includes a lab-oriented page.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present. The evidence comes from an active lab-style page.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. Affiliation evidence relies on a lab page rather than a faculty profile.
- confidence: `0.66`

### 244. Eli Upfal (Brown University)

- Rank: `52`
- Department: `Brown University Department of Computer Science`
- Faculty URL: `https://cs.brown.edu/people/eli`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `44`
- ra_score: `32`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics. Research description is explicit.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 245. Hui Fang 0001 (University of Delaware)

- Rank: `70`
- Department: `Computer & Information Sciences at the University of Delaware`
- Faculty URL: `http://www.ece.udel.edu/~hfang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `44`
- ra_score: `32`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics. Research description is explicit.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 246. John D. Kececioglu (University of Arizona)

- Rank: `83`
- Department: `University of Arizona Department of Computer Science | Computer Science`
- Faculty URL: `https://www.cs.arizona.edu/~kece`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `44`
- ra_score: `32`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics. Research description is explicit.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 247. Ophir Frieder (Georgetown University)

- Rank: `86`
- Department: `Department of Computer Science`
- Faculty URL: `http://people.cs.georgetown.edu/~ophir`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `44`
- ra_score: `32`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics. Research description is explicit.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 248. Juyang Weng (Michigan State University)

- Rank: `67`
- Department: `Computer Science and Engineering | College of Engineering`
- Faculty URL: `http://www.cse.msu.edu/~weng`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `42`
- ra_score: `44`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 249. Lijun Yin 0001 (Binghamton University)

- Rank: `70`
- Department: `School of Computing`
- Faculty URL: `http://www.cs.binghamton.edu/~lijun`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `42`
- ra_score: `44`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 250. Andrew R. Willis (UNC - Charlotte)

- Rank: `75`
- Department: `Homepage - College of Computing and Informatics`
- Faculty URL: `https://ece.charlotte.edu/directory/dr-andrew-r-willis-phd`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `42`
- ra_score: `44`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 251. Chandra Kambhamettu (University of South Florida)

- Rank: `80`
- Department: `Bellini College of Artificial Intelligence, Cybersecurity and Computing`
- Faculty URL: `https://www.usf.edu/ai-cybersecurity-computing/people/faculty/chandra_kambhamettu.aspx`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `42`
- ra_score: `44`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 252. Sourya Roy (University of Iowa)

- Rank: `97`
- Department: `Computer Science | College of Liberal Arts and Sciences | The University of Iowa`
- Faculty URL: `https://cs.uiowa.edu/people/sourya-roy`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `42`
- ra_score: `44`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 253. Qing Yang 0003 (University of North Texas)

- Rank: `97`
- Department: `Computer Science and Engineering`
- Faculty URL: `https://facultyinfo.unt.edu/faculty-profile?profile=qy0022`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `42`
- ra_score: `44`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 254. Chengjun Liu (NJIT)

- Rank: `63`
- Department: `Home | Department of Computer Science`
- Faculty URL: `http://cs.njit.edu/liu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `42`
- ra_score: `42`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision, NLP / language models.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision, NLP / language models.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 255. David A. McAllester (TTI Chicago)

- Rank: `89`
- Department: `TTI Chicago`
- Faculty URL: `http://ttic.uchicago.edu/~dmcallester`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `42`
- ra_score: `42`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision, NLP / language models.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision, NLP / language models.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 256. David McAllester (TTI Chicago)

- Rank: `89`
- Department: `TTI Chicago`
- Faculty URL: `http://ttic.uchicago.edu/~dmcallester`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `42`
- ra_score: `42`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision, NLP / language models.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision, NLP / language models.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 257. Yanhua Li (Worcester Polytechnic Institute)

- Rank: `75`
- Department: `Computer Science`
- Faculty URL: `http://www.wpi.edu/~yli15`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues present.
- phd_score: `41`
- ra_score: `63`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.83`

### 258. George K. Atia (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `http://eecs.ucf.edu/~atia`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `41`
- ra_score: `38`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 259. Ozlem O. Garibay (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `https://www.cecs.ucf.edu/faculty/ozlem-ozmen-garibay`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `41`
- ra_score: `38`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 260. Chongjie Zhang (Washington University in St. Louis)

- Rank: `58`
- Department: `Home | WashU Computer Science & Engineering`
- Faculty URL: `https://engineering.washu.edu/faculty/Chongjie-Zhang.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `41`
- ra_score: `38`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 261. Alina Zare (University of Florida)

- Rank: `59`
- Department: `Department of Computer & Information Science & Engineering`
- Faculty URL: `https://faculty.eng.ufl.edu/machine-learning/people/faculty`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `41`
- ra_score: `38`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 262. Mai Vu (Tufts University)

- Rank: `70`
- Department: `Homepage | Department of Computer Science`
- Faculty URL: `https://engineering.tufts.edu/cs/people/faculty/mai-vu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `41`
- ra_score: `38`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 263. Misha Elena Kilmer (Tufts University)

- Rank: `70`
- Department: `Homepage | Department of Computer Science`
- Faculty URL: `https://engineering.tufts.edu/cs/people/faculty/misha-kilmer`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `41`
- ra_score: `38`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 264. Ákos Lédeczi (Vanderbilt University)

- Rank: `70`
- Department: `Department of Computer Science - School of EngineeringSchool of Engineering`
- Faculty URL: `https://www.isis.vanderbilt.edu/akos`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `41`
- ra_score: `38`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 265. Anita Raja (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `https://anraja.commons.gc.cuny.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `41`
- ra_score: `38`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 266. Anupam Joshi (Univ. of Maryland - Baltimore County)

- Rank: `89`
- Department: `Department of Computer Science and Electrical Engineering – UMBC`
- Faculty URL: `http://www.csee.umbc.edu/~joshi`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `41`
- ra_score: `38`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 267. Mustafa Bilgic 0001 (Illinois Institute of Technology)

- Rank: `97`
- Department: `Computer Science`
- Faculty URL: `https://science.iit.edu/people/faculty/mustafa-bilgic`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `41`
- ra_score: `38`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 268. Yue Dai 0005 (Illinois Institute of Technology)

- Rank: `97`
- Department: `Computer Science`
- Faculty URL: `https://www.iit.edu/directory/people/yue-dai`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `41`
- ra_score: `38`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 269. Yutong Wang 0002 (Illinois Institute of Technology)

- Rank: `97`
- Department: `Computer Science`
- Faculty URL: `https://www.iit.edu/directory/people/yutong-wang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `41`
- ra_score: `38`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.71`

### 270. Rahul Sarpeshkar (Dartmouth College)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `https://engineering.dartmouth.edu/community/faculty/rahul-sarpeshkar`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `40`
- ra_score: `42`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics. Recent activity cues are present.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.39`

### 271. Jun Wang 0001 (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `http://www.cass.eecs.ucf.edu/?page_id=1249`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues present.
- phd_score: `38`
- ra_score: `53`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.83`

### 272. Fan Chen 0001 (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `https://homes.luddy.indiana.edu/fc7`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues present.
- phd_score: `38`
- ra_score: `53`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.83`

### 273. Roni Khardon (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `http://homes.sice.indiana.edu/rkhardon`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues present.
- phd_score: `38`
- ra_score: `53`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.83`

### 274. Nikhil Muralidhar (Stevens Institute of Technology)

- Rank: `70`
- Department: `Department of Computer Science | External Site (Under Construction)`
- Faculty URL: `https://www.stevens.edu/profile/nmurali1`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues present.
- phd_score: `38`
- ra_score: `53`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.83`

### 275. Guoquan Huang 0001 (University of Delaware)

- Rank: `70`
- Department: `Computer & Information Sciences at the University of Delaware`
- Faculty URL: `https://udel.edu/~ghuang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues present.
- phd_score: `38`
- ra_score: `53`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.83`

### 276. George Dimitri Konidaris (Brown University)

- Rank: `52`
- Department: `Brown University Department of Computer Science`
- Faculty URL: `http://cs.brown.edu/people/gdk`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 277. Yu Cheng 0002 (Brown University)

- Rank: `52`
- Department: `Brown University Department of Computer Science`
- Faculty URL: `http://cs.brown.edu/people/ycheng79`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 278. Xiaoli Z. Fern (Oregon State University)

- Rank: `53`
- Department: `Electrical Engineering and Computer Science | College of Engineering`
- Faculty URL: `http://web.engr.oregonstate.edu/~xfern`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 279. Nazanin Rahnavard (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `http://cwnlab.eecs.ucf.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 280. Eleftherios Garyfallidis (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `https://grg.sice.indiana.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 281. Christopher Homan (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `https://www.cs.rit.edu/~cmh`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 282. My T. Thai (University of Florida)

- Rank: `59`
- Department: `Department of Computer & Information Science & Engineering`
- Faculty URL: `http://www.cise.ufl.edu/~mythai`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 283. Patrick Traynor (University of Florida)

- Rank: `59`
- Department: `Department of Computer & Information Science & Engineering`
- Faculty URL: `https://www.cise.ufl.edu/~traynor`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 284. Tim Weninger (University of Notre Dame)

- Rank: `59`
- Department: `Home - Computer Science and Engineering`
- Faculty URL: `https://www3.nd.edu/~tweninge`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 285. Xiangliang Zhang 0001 (University of Notre Dame)

- Rank: `59`
- Department: `Home - Computer Science and Engineering`
- Faculty URL: `https://engineering.nd.edu/faculty/xiangliang-zhang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 286. Gourab Ghoshal (University of Rochester)

- Rank: `59`
- Department: `Department of Computer Science : University of Rochester`
- Faculty URL: `http://gghoshal.pas.rochester.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 287. Michael C. Huang 0001 (University of Rochester)

- Rank: `59`
- Department: `Department of Computer Science : University of Rochester`
- Faculty URL: `http://www.ece.rochester.edu/~mihuang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 288. Christophe Hauser (Dartmouth College)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `https://web.cs.dartmouth.edu/people/christophe-hauser`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 289. Nikhil Singh 0003 (Dartmouth College)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `https://nsingh1.host.dartmouth.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 290. Cristian Borcea (NJIT)

- Rank: `63`
- Department: `Home | Department of Computer Science`
- Faculty URL: `http://cs.njit.edu/~borcea`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 291. Jingtao Wang (University of Pittsburgh)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `https://people.cs.pitt.edu/~jingtaow`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 292. Konstantinos Pelechrinis (University of Pittsburgh)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `http://www.pitt.edu/~kpele`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 293. Peter Brusilovsky (University of Pittsburgh)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `http://www.pitt.edu/~peterb`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 294. Shibo Li (Florida State University)

- Rank: `67`
- Department: `DEPARTMENT OF COMPUTER SCIENCE – College of Arts and Sciences`
- Faculty URL: `https://www.cs.fsu.edu/department/faculty/shiboli`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 295. Yushun Dong (Florida State University)

- Rank: `67`
- Department: `DEPARTMENT OF COMPUTER SCIENCE – College of Arts and Sciences`
- Faculty URL: `https://www.cs.fsu.edu/department/faculty/dong`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 296. Pang-Ning Tan (Michigan State University)

- Rank: `67`
- Department: `Computer Science and Engineering | College of Engineering`
- Faculty URL: `http://www.cse.msu.edu/~ptan`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 297. Weiyi Meng (Binghamton University)

- Rank: `70`
- Department: `School of Computing`
- Faculty URL: `http://www.cs.binghamton.edu/~meng`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 298. Jivko Sinapov (Tufts University)

- Rank: `70`
- Department: `Homepage | Department of Computer Science`
- Faculty URL: `https://www.eecs.tufts.edu/~jsinapov`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 299. Berk Çalli (Worcester Polytechnic Institute)

- Rank: `75`
- Department: `Computer Science`
- Faculty URL: `https://www.wpi.edu/people/faculty/bcalli`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 300. Yaser S. Abu-Mostafa (California Inst. of Technology)

- Rank: `80`
- Department: `Computing + Mathematical Sciences`
- Faculty URL: `https://work.caltech.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 301. Lin Yan 0003 (Iowa State University)

- Rank: `80`
- Department: `Department of Computer Science`
- Faculty URL: `https://www.cs.iastate.edu/people/lin-yan`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 302. Prasant Mohapatra (University of South Florida)

- Rank: `80`
- Department: `Bellini College of Artificial Intelligence, Cybersecurity and Computing`
- Faculty URL: `https://pmlab.cse.usf.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 303. Yi Sheng 0001 (University of South Florida)

- Rank: `80`
- Department: `Bellini College of Artificial Intelligence, Cybersecurity and Computing`
- Faculty URL: `https://www.usf.edu/ai-cybersecurity-computing/people/faculty/yi_sheng.aspx`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 304. Lei Cao 0004 (University of Arizona)

- Rank: `83`
- Department: `University of Arizona Department of Computer Science | Computer Science`
- Faculty URL: `https://www.cs.arizona.edu/person/lei-cao`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 305. Marcus A. Maloof (Georgetown University)

- Rank: `86`
- Department: `Department of Computer Science`
- Faculty URL: `http://people.cs.georgetown.edu/~maloof`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 306. Marco Brocanelli (Wayne State University)

- Rank: `86`
- Department: `Wayne State University`
- Faculty URL: `http://brok.eng.wayne.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 307. Prashant Khanduri (Wayne State University)

- Rank: `86`
- Department: `Wayne State University`
- Faculty URL: `https://engineering.wayne.edu/profile/hm8920`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 308. RhongHo Jang (Wayne State University)

- Rank: `86`
- Department: `Wayne State University`
- Faculty URL: `https://engineering.wayne.edu/profile/hf8512`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 309. Jason Liu (Florida International University)

- Rank: `89`
- Department: `Knight Foundation School of Computing and Information Sciences`
- Faculty URL: `http://www.cis.fiu.edu/~liux`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 310. Alex Gittens (Rensselaer Polytechnic Institute)

- Rank: `89`
- Department: `Computer Science`
- Faculty URL: `http://www.cs.rpi.edu/~gittea`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 311. Chen Wang 0027 (Rensselaer Polytechnic Institute)

- Rank: `89`
- Department: `Computer Science`
- Faculty URL: `https://faculty.rpi.edu/chen-wang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 312. James R. Foulds (Univ. of Maryland - Baltimore County)

- Rank: `89`
- Department: `Department of Computer Science and Electrical Engineering – UMBC`
- Faculty URL: `https://jfoulds.informationsystems.umbc.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 313. Tim Finin (Univ. of Maryland - Baltimore County)

- Rank: `89`
- Department: `Department of Computer Science and Electrical Engineering – UMBC`
- Faculty URL: `http://umbc.edu/~finin`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 314. Jeff Heflin (Lehigh University)

- Rank: `97`
- Department: `Computer Science & Engineering | P.C. Rossin College of Engineering & Applied Science`
- Faculty URL: `http://www.cse.lehigh.edu/~heflin`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 315. Lifang He 0001 (Lehigh University)

- Rank: `97`
- Department: `Computer Science & Engineering | P.C. Rossin College of Engineering & Applied Science`
- Faculty URL: `https://engineering.lehigh.edu/faculty/lifang-he`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 316. Sihong Xie (Lehigh University)

- Rank: `97`
- Department: `Computer Science & Engineering | P.C. Rossin College of Engineering & Applied Science`
- Faculty URL: `http://www.cse.lehigh.edu/~sxie`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 317. Bijaya Adhikari (University of Iowa)

- Rank: `97`
- Department: `Computer Science | College of Liberal Arts and Sciences | The University of Iowa`
- Faculty URL: `https://cs.uiowa.edu/people/bijaya-adhikari`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 318. Mehrdad Moharrami (University of Iowa)

- Rank: `97`
- Department: `Computer Science | College of Liberal Arts and Sciences | The University of Iowa`
- Faculty URL: `https://cs.uiowa.edu/people/mehrdad-moharrami`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 319. Rishab Nithyanand (University of Iowa)

- Rank: `97`
- Department: `Computer Science | College of Liberal Arts and Sciences | The University of Iowa`
- Faculty URL: `https://cs.uiowa.edu/people/rishab-nithyanand`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 320. Ramakrishnan Durairajan (University of Oregon)

- Rank: `97`
- Department: `Computer Science | School of Computer and Data Sciences`
- Faculty URL: `http://ix.cs.uoregon.edu/~ram`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 321. Thanh Hong Nguyen (University of Oregon)

- Rank: `97`
- Department: `Computer Science | School of Computer and Data Sciences`
- Faculty URL: `https://ix.cs.uoregon.edu/~thanhhng`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 322. Ellie Pavlick (Brown University)

- Rank: `52`
- Department: `Brown University Department of Computer Science`
- Faculty URL: `https://cs.brown.edu/people/epavlick/index.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `26`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 323. Dan I. Moldovan (University of Texas at Dallas)

- Rank: `55`
- Department: `UT Dallas SSO Login`
- Faculty URL: `http://cs.utdallas.edu/people/faculty/moldovan-dan`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `26`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 324. Janyce Wiebe (University of Pittsburgh)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `https://people.cs.pitt.edu/~wiebe`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `26`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 325. Forrest Sheng Bao (Iowa State University)

- Rank: `80`
- Department: `Department of Computer Science`
- Faculty URL: `https://www.cs.iastate.edu/people/forrest-sheng-bao`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `26`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 326. Dongsheng Ding (University of Tennessee)

- Rank: `89`
- Department: `University of Tennessee`
- Faculty URL: `https://eecs.utk.edu/people/dongsheng-ding`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `26`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 327. Rebecca Hwa (George Washington University)

- Rank: `97`
- Department: `Department of Computer Science | School of Engineering & Applied Science | The George Washington University`
- Faculty URL: `https://cs.engineering.gwu.edu/rebecca-hwa`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `38`
- ra_score: `26`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 328. Varsha Dani (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `https://www.rit.edu/directory/vxdvcs-varsha-dani`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `36`
- ra_score: `26`
- rationale_phd: Explicit overlap found in: computer vision. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 329. Patrick J. Flynn (University of Notre Dame)

- Rank: `59`
- Department: `Home - Computer Science and Engineering`
- Faculty URL: `http://www3.nd.edu/~flynn`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `36`
- ra_score: `26`
- rationale_phd: Explicit overlap found in: computer vision. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 330. Ioannis Stamos (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `http://www.cs.hunter.cuny.edu/~ioannis`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `36`
- ra_score: `26`
- rationale_phd: Explicit overlap found in: computer vision. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 331. Adam W. Bargteil (Univ. of Maryland - Baltimore County)

- Rank: `89`
- Department: `Department of Computer Science and Electrical Engineering – UMBC`
- Faculty URL: `http://www.csee.umbc.edu/~adamb`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `36`
- ra_score: `26`
- rationale_phd: Explicit overlap found in: computer vision. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 332. Kristen Johnson (Michigan State University)

- Rank: `67`
- Department: `Computer Science and Engineering | College of Engineering`
- Faculty URL: `https://www.egr.msu.edu/people/profile/kristenj`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues present; RA cues present.
- phd_score: `35`
- ra_score: `45`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.73`

### 333. Sijia Liu 0001 (Michigan State University)

- Rank: `67`
- Department: `Computer Science and Engineering | College of Engineering`
- Faculty URL: `https://www.egr.msu.edu/people/profile/liusiji5`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues present; RA cues present.
- phd_score: `35`
- ra_score: `45`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.73`

### 334. Yanni Sun (Michigan State University)

- Rank: `67`
- Department: `Computer Science and Engineering | College of Engineering`
- Faculty URL: `https://www.egr.msu.edu/people/profile/yannisun`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues present; RA cues present.
- phd_score: `35`
- ra_score: `45`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.73`

### 335. Grace Hui Yang (Georgetown University)

- Rank: `86`
- Department: `Department of Computer Science`
- Faculty URL: `http://infosense.cs.georgetown.edu/grace`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues present; RA cues UNKNOWN.
- phd_score: `35`
- ra_score: `20`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.73`

### 336. Chiu C. Tan 0001 (Temple University)

- Rank: `89`
- Department: `Department of Computer & Information Sciences | College of Science and Technology`
- Faculty URL: `https://cis.temple.edu/~cctan`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues present; RA cues UNKNOWN.
- phd_score: `35`
- ra_score: `20`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.61`

### 337. Toby Jia-Jun Li (University of Notre Dame)

- Rank: `59`
- Department: `Home - Computer Science and Engineering`
- Faculty URL: `https://cse.nd.edu/faculty/toby-jia-jun-li`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues present.
- phd_score: `34`
- ra_score: `61`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 338. Guangmo Tong (University of Delaware)

- Rank: `70`
- Department: `Computer & Information Sciences at the University of Delaware`
- Faculty URL: `https://udel.edu/~amotong`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues present.
- phd_score: `34`
- ra_score: `61`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 339. Karen Livescu (TTI Chicago)

- Rank: `89`
- Department: `TTI Chicago`
- Faculty URL: `http://ttic.uchicago.edu/~klivescu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues present.
- phd_score: `34`
- ra_score: `61`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 340. Alan Wang (Oregon State University)

- Rank: `53`
- Department: `Electrical Engineering and Computer Science | College of Engineering`
- Faculty URL: `http://eecs.oregonstate.edu/people/wang-alan`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 341. Fuxin Li (Oregon State University)

- Rank: `53`
- Department: `Electrical Engineering and Computer Science | College of Engineering`
- Faculty URL: `http://eecs.oregonstate.edu/people/li-fuxin`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 342. Glencora Borradaile (Oregon State University)

- Rank: `53`
- Department: `Electrical Engineering and Computer Science | College of Engineering`
- Faculty URL: `http://eecs.oregonstate.edu/people/borradaile-glencora`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 343. Julie A. Adams (Oregon State University)

- Rank: `53`
- Department: `Electrical Engineering and Computer Science | College of Engineering`
- Faculty URL: `http://eecs.oregonstate.edu/people/adams-julie`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 344. Rakesh Bobba (Oregon State University)

- Rank: `53`
- Department: `Electrical Engineering and Computer Science | College of Engineering`
- Faculty URL: `http://eecs.oregonstate.edu/people/bobba-rakesh`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 345. Weng-Keen Wong (Oregon State University)

- Rank: `53`
- Department: `Electrical Engineering and Computer Science | College of Engineering`
- Faculty URL: `http://eecs.oregonstate.edu/people/wong-weng-keen`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 346. Bhavani Thuraisingham (University of Texas at Dallas)

- Rank: `55`
- Department: `UT Dallas SSO Login`
- Faculty URL: `http://www.utdallas.edu/~bhavani.thuraisingham`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 347. M. Mustafa Rafique (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `https://cs.rit.edu/~mrafique`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 348. Daniel Gildea (University of Rochester)

- Rank: `59`
- Department: `Department of Computer Science : University of Rochester`
- Faculty URL: `https://www.cs.rochester.edu/u/gildea`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 349. Patrick H. Chen (Binghamton University)

- Rank: `70`
- Department: `School of Computing`
- Faculty URL: `https://www.binghamton.edu/computer-science/people/profile.html?id=patrickchen`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 350. Matthew Johnson-Roberson (Vanderbilt University)

- Rank: `70`
- Department: `Department of Computer Science - School of EngineeringSchool of Engineering`
- Faculty URL: `https://news.vanderbilt.edu/tag/matthew-johnson-roberson`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 351. Yiwei Wang 0001 (Univ. of California - Merced)

- Rank: `75`
- Department: `Computer Science & Engineering (CSE) | School of Engineering`
- Faculty URL: `https://engineering.ucmerced.edu/content/yiwei-wang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 352. Mengdi Huai (Iowa State University)

- Rank: `80`
- Department: `Department of Computer Science`
- Faculty URL: `https://www.cs.iastate.edu/people/mengdi-huai`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 353. Qi Li 0012 (Iowa State University)

- Rank: `80`
- Department: `Department of Computer Science`
- Faculty URL: `https://www.cs.iastate.edu/people/qi-li`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 354. Yang Li 0183 (Iowa State University)

- Rank: `80`
- Department: `Department of Computer Science`
- Faculty URL: `https://www.cs.iastate.edu/people/yang-li`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 355. Li Xiong 0001 (Emory University)

- Rank: `83`
- Department: `The Department of Computer Science`
- Faculty URL: `https://cs.emory.edu/~lxiong`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 356. Ellen Riloff (University of Arizona)

- Rank: `83`
- Department: `University of Arizona Department of Computer Science | Computer Science`
- Faculty URL: `https://www.cs.arizona.edu/person/ellen-riloff`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 357. Alla Rozovskaya (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `https://www.cs.qc.cuny.edu/rozovskaya.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 358. Neng-Fa Zhou (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `http://www.sci.brooklyn.cuny.edu/~zhou`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 359. Dongsheng Luo (Florida International University)

- Rank: `89`
- Department: `Knight Foundation School of Computing and Information Sciences`
- Faculty URL: `https://users.cs.fiu.edu/~dluo`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 360. Sagnik Ray Choudhury (University of North Texas)

- Rank: `97`
- Department: `Computer Science and Engineering`
- Faculty URL: `https://facultyinfo.unt.edu/faculty-profile?profile=sr2004`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `36`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 361. Nathan D. Cahill (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `https://people.rit.edu/ndcsma`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `34`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 362. Zhongfei Zhang (Binghamton University)

- Rank: `70`
- Department: `School of Computing`
- Faculty URL: `http://www.cs.binghamton.edu/~zhongfei`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `34`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 363. Gregory Shakhnarovich (TTI Chicago)

- Rank: `89`
- Department: `TTI Chicago`
- Faculty URL: `http://ttic.uchicago.edu/~gregory`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `34`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 364. J. Ross Beveridge (Colorado State University)

- Rank: `97`
- Department: `Department of Computer Science | CSU – Department of Computer Science at Colorado State University`
- Faculty URL: `http://www.cs.colostate.edu/~ross`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `34`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 365. Xinrui Cui (University of North Texas)

- Rank: `97`
- Department: `Computer Science and Engineering`
- Faculty URL: `https://computerscience.engineering.unt.edu/people/faculty/xinrui-cui`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `34`
- ra_score: `34`
- rationale_phd: Explicit overlap found in: general AI / ML, computer vision.
- rationale_ra: Relevant overlap found in: general AI / ML, computer vision.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 366. Prasad Tadepalli (Oregon State University)

- Rank: `53`
- Department: `Electrical Engineering and Computer Science | College of Engineering`
- Faculty URL: `http://eecs.oregonstate.edu/~tadepall`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `33`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.59`

### 367. Fillia Makedon (University of Texas at Arlington)

- Rank: `59`
- Department: `Computer Science and Engineering - The University of Texas at Arlington`
- Faculty URL: `http://heracleia.uta.edu/~makedon`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `33`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.59`

### 368. Abiy Tasissa (Tufts University)

- Rank: `70`
- Department: `Homepage | Department of Computer Science`
- Faculty URL: `https://engineering.tufts.edu/cs/people/faculty/abiy-tasissa`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `33`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.59`

### 369. Shuchin Aeron (Tufts University)

- Rank: `70`
- Department: `Homepage | Department of Computer Science`
- Faculty URL: `https://engineering.tufts.edu/cs/people/faculty/shuchin-aeron`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues present; RA cues UNKNOWN.
- phd_score: `33`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Advising or prospective-student cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Student-mentoring cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.59`

### 370. Yu Kong 0001 (Michigan State University)

- Rank: `67`
- Department: `Computer Science and Engineering | College of Engineering`
- Faculty URL: `https://www.egr.msu.edu/~yukong`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computer vision, NLP / language models; advising cues UNKNOWN; RA cues present.
- phd_score: `32`
- ra_score: `59`
- rationale_phd: Explicit overlap found in: computer vision, NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computer vision, NLP / language models. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 371. Ion I. Mandoiu (University of Connecticut)

- Rank: `63`
- Department: `Home | School of Computing | College of Engineering`
- Faculty URL: `http://www.engr.uconn.edu/~ion`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `32`
- ra_score: `32`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 372. Oliver Eulenstein (Iowa State University)

- Rank: `80`
- Department: `Department of Computer Science`
- Faculty URL: `http://www.cs.iastate.edu/~oeulenst`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computational biology / bioinformatics; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `32`
- ra_score: `32`
- rationale_phd: Explicit overlap found in: computational biology / bioinformatics.
- rationale_ra: Relevant overlap found in: computational biology / bioinformatics.
- potential_concerns: No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 373. Nora Ayanian (Brown University)

- Rank: `52`
- Department: `Brown University Department of Computer Science`
- Faculty URL: `https://vivo.brown.edu/display/nayanian`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `30`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 374. Stefanie Tellex (Brown University)

- Rank: `52`
- Department: `Brown University Department of Computer Science`
- Faculty URL: `https://cs.brown.edu/people/stellex`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `30`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 375. Ivan Garibay (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `https://www.cs.ucf.edu/~garibay`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `30`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 376. Nicholas Ruozzi (University of Texas at Dallas)

- Rank: `55`
- Department: `UT Dallas SSO Login`
- Faculty URL: `http://cs.utdallas.edu/people/faculty/nicholas-ruozzi`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `30`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 377. Manfred Huber (University of Texas at Arlington)

- Rank: `59`
- Department: `Computer Science and Engineering - The University of Texas at Arlington`
- Faculty URL: `http://ranger.uta.edu/~huber`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `30`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 378. James Geller (NJIT)

- Rank: `63`
- Department: `Home | Department of Computer Science`
- Faculty URL: `https://web.njit.edu/~geller`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `30`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 379. Yingxue Zhang 0002 (Binghamton University)

- Rank: `70`
- Department: `School of Computing`
- Faculty URL: `https://www.binghamton.edu/computer-science/people/profile.html?id=yzhang42`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `30`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 380. Zhen Xie (Binghamton University)

- Rank: `70`
- Department: `School of Computing`
- Faculty URL: `https://www.binghamton.edu/computer-science/people/profile.html?id=zxie3`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `30`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 381. Xiangnan Kong (Worcester Polytechnic Institute)

- Rank: `75`
- Department: `Computer Science`
- Faculty URL: `https://www.wpi.edu/people/faculty/xkong`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `30`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 382. Frederick Eberhardt (California Inst. of Technology)

- Rank: `80`
- Department: `Computing + Mathematical Sciences`
- Faculty URL: `http://www.its.caltech.edu/~fehardt`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `30`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 383. Diane J. Cook (Washington State University)

- Rank: `86`
- Department: `School of Electrical Engineering & Computer Science`
- Faculty URL: `http://www.eecs.wsu.edu/~cook`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `30`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 384. Keke Chen (Univ. of Maryland - Baltimore County)

- Rank: `89`
- Department: `Department of Computer Science and Electrical Engineering – UMBC`
- Faculty URL: `https://www.csee.umbc.edu/keke-chen`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `30`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 385. Penny Rheingans (Univ. of Maryland - Baltimore County)

- Rank: `89`
- Department: `Department of Computer Science and Electrical Engineering – UMBC`
- Faculty URL: `http://www.csee.umbc.edu/~rheingan`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `30`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 386. Carlos Ordonez 0001 (University of Houston)

- Rank: `97`
- Department: `University of Houston`
- Faculty URL: `http://www2.cs.uh.edu/~ordonez`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `30`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 387. Ian Parberry (University of North Texas)

- Rank: `97`
- Department: `Computer Science and Engineering`
- Faculty URL: `http://larc.unt.edu/ian`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `30`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 388. Jing Yuan 0002 (University of North Texas)

- Rank: `97`
- Department: `Computer Science and Engineering`
- Faculty URL: `https://computerscience.engineering.unt.edu/people/faculty/jing-yuan`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `30`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 389. Weishi Shi (University of North Texas)

- Rank: `97`
- Department: `Computer Science and Engineering`
- Faculty URL: `https://computerscience.engineering.unt.edu/people/faculty/weishi-shi`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `30`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 390. Daniel Lowd (University of Oregon)

- Rank: `97`
- Department: `Computer Science | School of Computer and Data Sciences`
- Faculty URL: `https://ix.cs.uoregon.edu/~lowd`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `30`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML. Research description is explicit.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 391. Shangqian Gao (Florida State University)

- Rank: `67`
- Department: `DEPARTMENT OF COMPUTER SCIENCE – College of Arts and Sciences`
- Faculty URL: `https://www.cs.fsu.edu/department/faculty/sgao`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `28`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: NLP / language models. Research description is explicit. Recent work cues are present.
- rationale_ra: Relevant overlap found in: NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 392. Elke A. Rundensteiner (Worcester Polytechnic Institute)

- Rank: `75`
- Department: `Computer Science`
- Faculty URL: `http://davis.wpi.edu/dsrg/MEMBERS/rundenst`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues present; RA cues present.
- phd_score: `27`
- ra_score: `35`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Advising or prospective-student cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. RA or recruiting cues are explicit. Student-mentoring cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains.
- confidence: `0.61`

### 393. Yuzhang Shang (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `https://www.ucf.edu/expert/yuzhang-shang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues present.
- phd_score: `26`
- ra_score: `53`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 394. Feng Luo 0001 (Clemson University)

- Rank: `75`
- Department: `School of Computing`
- Faculty URL: `https://people.cs.clemson.edu/~luofeng`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues present.
- phd_score: `26`
- ra_score: `53`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 395. Jie Wu 0001 (Temple University)

- Rank: `89`
- Department: `Department of Computer & Information Sciences | College of Science and Technology`
- Faculty URL: `https://cis.temple.edu/~wu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues present.
- phd_score: `26`
- ra_score: `53`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 396. Peng Jiang 0004 (University of Iowa)

- Rank: `97`
- Department: `Computer Science | College of Liberal Arts and Sciences | The University of Iowa`
- Faculty URL: `https://homepage.divms.uiowa.edu/~penjiang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues present.
- phd_score: `26`
- ra_score: `53`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 397. Yunhe Feng (University of North Texas)

- Rank: `97`
- Department: `Computer Science and Engineering`
- Faculty URL: `https://computerscience.engineering.unt.edu/people/faculty/yunhe-feng`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues present.
- phd_score: `26`
- ra_score: `53`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 398. Rickard Ewetz (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `http://www.ece.ucf.edu/~ewetz`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 399. Zhenyi Wang 0001 (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `https://www.ucf.edu/expert/zhenyi-wang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 400. Andrew Meneely (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `http://www.se.rit.edu/~andy`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 401. Ivona Bezáková (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `https://www.cs.rit.edu/~ib`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 402. Peizhao Hu (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `https://www.cs.rit.edu/~ph`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 403. Nitesh V. Chawla (University of Notre Dame)

- Rank: `59`
- Department: `Home - Computer Science and Engineering`
- Faculty URL: `http://www3.nd.edu/~nchawla`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 404. Alberto Quattrini Li (Dartmouth College)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `https://web.cs.dartmouth.edu/people/alberto-quattrini-li`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 405. Daniel N. Rockmore (Dartmouth College)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `http://www.cs.dartmouth.edu/~rockmore`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 406. Baruch Schieber (NJIT)

- Rank: `63`
- Department: `Home | Department of Computer Science`
- Faculty URL: `https://cs.njit.edu/faculty/sbar`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 407. Youtao Zhang (University of Pittsburgh)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `https://cs.pitt.edu/~zhangyt`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 408. Jiliang Tang (Michigan State University)

- Rank: `67`
- Department: `Computer Science and Engineering | College of Engineering`
- Faculty URL: `http://www.cse.msu.edu/~tangjili`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 409. Anselm Blumer (Tufts University)

- Rank: `70`
- Department: `Homepage | Department of Computer Science`
- Faculty URL: `http://www.cs.tufts.edu/~ablumer`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 410. Donna K. Slonim (Tufts University)

- Rank: `70`
- Department: `Homepage | Department of Computer Science`
- Faculty URL: `http://www.cs.tufts.edu/~slonim`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 411. Vishesh Kumar (Vanderbilt University)

- Rank: `70`
- Department: `Department of Computer Science - School of EngineeringSchool of Engineering`
- Faculty URL: `https://lab.vanderbilt.edu/live/person/vishesh-kumar`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 412. Hamed Tabkhi (UNC - Charlotte)

- Rank: `75`
- Department: `Homepage - College of Computing and Informatics`
- Faculty URL: `https://ece.charlotte.edu/directory/dr-hamed-tabkhi-phd`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 413. Jeremy Holleman (UNC - Charlotte)

- Rank: `75`
- Department: `Homepage - College of Computing and Informatics`
- Faculty URL: `https://ece.charlotte.edu/directory/dr-jeremy-holleman-phd`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 414. Yong Zhang (UNC - Charlotte)

- Rank: `75`
- Department: `Homepage - College of Computing and Informatics`
- Faculty URL: `https://ece.charlotte.edu/directory/dr-yong-zhang-phd`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 415. David C. Noelle (Univ. of California - Merced)

- Rank: `75`
- Department: `Computer Science & Engineering (CSE) | School of Engineering`
- Faculty URL: `https://eecs.ucmerced.edu/content/david-noelle`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 416. Charles Rich (Worcester Polytechnic Institute)

- Rank: `75`
- Department: `Computer Science`
- Faculty URL: `http://www.cs.wpi.edu/~rich`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 417. Alan H. Barr (California Inst. of Technology)

- Rank: `80`
- Department: `Computing + Mathematical Sciences`
- Faculty URL: `http://www.eas.caltech.edu/people/2923/profile`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 418. Anima Anandkumar (California Inst. of Technology)

- Rank: `80`
- Department: `Computing + Mathematical Sciences`
- Faculty URL: `http://tensorlab.cms.caltech.edu/users/anima`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 419. Erik Winfree (California Inst. of Technology)

- Rank: `80`
- Department: `Computing + Mathematical Sciences`
- Faculty URL: `http://www.dna.caltech.edu/~winfree`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 420. Joel A. Tropp (California Inst. of Technology)

- Rank: `80`
- Department: `Computing + Mathematical Sciences`
- Faculty URL: `http://users.cms.caltech.edu/~jtropp`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 421. Steven H. Low (California Inst. of Technology)

- Rank: `80`
- Department: `Computing + Mathematical Sciences`
- Faculty URL: `http://www.eas.caltech.edu/people/3109/profile`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 422. Aduri Pavan (Iowa State University)

- Rank: `80`
- Department: `Department of Computer Science`
- Faculty URL: `http://www.cs.iastate.edu/people/pavan-aduri`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 423. Yao Liu 0007 (University of South Florida)

- Rank: `80`
- Department: `Bellini College of Artificial Intelligence, Cybersecurity and Computing`
- Faculty URL: `http://www.cse.usf.edu/~yliu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 424. Kobbi Nissim (Georgetown University)

- Rank: `86`
- Department: `Department of Computer Science`
- Faculty URL: `http://people.cs.georgetown.edu/~kobbi`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 425. Sarah Zelikovitz (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `http://www.cs.csi.cuny.edu/~zelikovi`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 426. Santiago Ontañón (Drexel University)

- Rank: `89`
- Department: `Computer Science Department | Drexel CCI`
- Faculty URL: `http://drexel.edu/cci/contact/Faculty/Ontanon-Santiago`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 427. Vasilis Gkatzelis (Drexel University)

- Rank: `89`
- Department: `Computer Science Department | Drexel CCI`
- Faculty URL: `https://www.cs.drexel.edu/~gkatz`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 428. James A. Hendler (Rensselaer Polytechnic Institute)

- Rank: `89`
- Department: `Computer Science`
- Faculty URL: `http://www.cs.rpi.edu/~hendler`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 429. Padmini Srinivasan (University of Iowa)

- Rank: `97`
- Department: `Computer Science | College of Liberal Arts and Sciences | The University of Iowa`
- Faculty URL: `https://cs.uiowa.edu/people/padmini-srinivasan`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 430. Weiran Wang (University of Iowa)

- Rank: `97`
- Department: `Computer Science | College of Liberal Arts and Sciences | The University of Iowa`
- Faculty URL: `https://cs.uiowa.edu/people/weiran-wang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 431. Mohammad Arif Ul Alam (University of Massachusetts Lowell)

- Rank: `97`
- Department: `Miner School of Computer and Information Sciences | Kennedy College of Sciences | UMass Lowell`
- Faculty URL: `http://faculty.uml.edu/~alam`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 432. Leen-Kiat Soh (University of Nebraska)

- Rank: `97`
- Department: `School of Computing | Nebraska`
- Faculty URL: `http://cse.unl.edu/~lksoh`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 433. Paul Tarau (University of North Texas)

- Rank: `97`
- Department: `Computer Science and Engineering`
- Faculty URL: `http://www.cse.unt.edu/~tarau`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 434. Rodney D. Nielsen (University of North Texas)

- Rank: `97`
- Department: `Computer Science and Engineering`
- Faculty URL: `http://www.cse.unt.edu/~nielsen`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 435. Song Fu (University of North Texas)

- Rank: `97`
- Department: `Computer Science and Engineering`
- Faculty URL: `http://www.cse.unt.edu/~song`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 436. Wei Jin 0006 (University of North Texas)

- Rank: `97`
- Department: `Computer Science and Engineering`
- Faculty URL: `http://www.cse.unt.edu/~weijin`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 437. Xiaohui Yuan (University of North Texas)

- Rank: `97`
- Department: `Computer Science and Engineering`
- Faculty URL: `http://www.cse.unt.edu/~xyuan`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 438. Xuan Guo (University of North Texas)

- Rank: `97`
- Department: `Computer Science and Engineering`
- Faculty URL: `http://www.cse.unt.edu/~xuanguo`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 439. Yan Huang 0002 (University of North Texas)

- Rank: `97`
- Department: `Computer Science and Engineering`
- Faculty URL: `http://www.cse.unt.edu/~huangyan`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 440. Zhuqing Liu (University of North Texas)

- Rank: `97`
- Department: `Computer Science and Engineering`
- Faculty URL: `https://facultyinfo.unt.edu/faculty-profile?profile=zl0223`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `28`
- rationale_phd: Explicit overlap found in: general AI / ML. Recent work cues are present.
- rationale_ra: Relevant overlap found in: general AI / ML. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 441. Suresh Venkatasubramanian (Brown University)

- Rank: `52`
- Department: `Brown University Department of Computer Science`
- Faculty URL: `https://vivo.brown.edu/display/suresh`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `26`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 442. Sandra Kübler (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `https://cl.indiana.edu/~skuebler`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `26`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 443. Tien N. Nguyen (University of Texas at Dallas)

- Rank: `55`
- Department: `UT Dallas SSO Login`
- Faculty URL: `http://www.utdallas.edu/~tien.n.nguyen`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `26`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 444. Sandra Carberry (University of Delaware)

- Rank: `70`
- Department: `Computer & Information Sciences at the University of Delaware`
- Faculty URL: `https://www.eecis.udel.edu/~carberry`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `26`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 445. Anna Rumshisky (University of Massachusetts Lowell)

- Rank: `97`
- Department: `Miner School of Computer and Information Sciences | Kennedy College of Sciences | UMass Lowell`
- Faculty URL: `http://www.cs.uml.edu/~arum`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML, NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `26`
- ra_score: `26`
- rationale_phd: Explicit overlap found in: general AI / ML, NLP / language models.
- rationale_ra: Relevant overlap found in: general AI / ML, NLP / language models.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 446. Eakta Jain (University of Florida)

- Rank: `59`
- Department: `Department of Computer & Information Science & Engineering`
- Faculty URL: `http://www.cise.ufl.edu/~ejain`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computer vision; advising cues UNKNOWN; RA cues present.
- phd_score: `24`
- ra_score: `51`
- rationale_phd: Explicit overlap found in: computer vision. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computer vision. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.71`

### 447. Rangachar Kasturi (University of South Florida)

- Rank: `80`
- Department: `Bellini College of Artificial Intelligence, Cybersecurity and Computing`
- Faculty URL: `http://www.cse.usf.edu/~r1k`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `24`
- ra_score: `26`
- rationale_phd: Explicit overlap found in: computer vision. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 448. George Wolberg (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `http://www-cs.ccny.cuny.edu/~wolberg`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `24`
- ra_score: `26`
- rationale_phd: Explicit overlap found in: computer vision. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 449. Badrinath Roysam (University of Houston)

- Rank: `97`
- Department: `University of Houston`
- Faculty URL: `http://www.ee.uh.edu/faculty/roysam`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `24`
- ra_score: `26`
- rationale_phd: Explicit overlap found in: computer vision. Recent work cues are present.
- rationale_ra: Relevant overlap found in: computer vision. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 450. Yuankai Huo (Vanderbilt University)

- Rank: `70`
- Department: `Department of Computer Science - School of EngineeringSchool of Engineering`
- Faculty URL: `https://my.vanderbilt.edu/huolab`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `23`
- ra_score: `45`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. Research fit evidence is sparse.
- confidence: `0.53`

### 451. Rong Ge 0002 (Clemson University)

- Rank: `75`
- Department: `School of Computing`
- Faculty URL: `https://people.cs.clemson.edu/~rge`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `23`
- ra_score: `45`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. RA or recruiting cues are explicit. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. Research fit evidence is sparse.
- confidence: `0.53`

### 452. Chen Yu 0001 (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `https://psych.indiana.edu/directory/faculty/yu-chen.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `23`
- ra_score: `20`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.41`

### 453. Amit Chakrabarti (Dartmouth College)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `https://www.cs.dartmouth.edu/~ac`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `23`
- ra_score: `20`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.41`

### 454. Alexandros Labrinidis (University of Pittsburgh)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `http://labrinidis.cs.pitt.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `23`
- ra_score: `20`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.41`

### 455. Yury Makarychev (TTI Chicago)

- Rank: `89`
- Department: `TTI Chicago`
- Faculty URL: `http://ttic.uchicago.edu/~yury`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `23`
- ra_score: `20`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present. Advising or prospective-student cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Student-mentoring cues are present. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.41`

### 456. Sherief Reda (Brown University)

- Rank: `52`
- Department: `Brown University Department of Computer Science`
- Faculty URL: `https://scale-lab.github.io/pages/sreda.html`
- Lab URL: `https://scale-lab.github.io/pages/sreda.html`
- Source Type: `lab_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `23`
- ra_score: `15`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present. Evidence includes a lab-oriented page.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present. The evidence comes from an active lab-style page.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Affiliation evidence relies on a lab page rather than a faculty profile.
- confidence: `0.44`

### 457. Netanel Raviv (Washington University in St. Louis)

- Rank: `58`
- Department: `Home | WashU Computer Science & Engineering`
- Faculty URL: `https://sites.wustl.edu/ravivlab`
- Lab URL: `https://sites.wustl.edu/ravivlab`
- Source Type: `lab_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `23`
- ra_score: `15`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present. Evidence includes a lab-oriented page.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present. The evidence comes from an active lab-style page.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Affiliation evidence relies on a lab page rather than a faculty profile.
- confidence: `0.44`

### 458. Lane A. Hemaspaandra (University of Rochester)

- Rank: `59`
- Department: `Department of Computer Science : University of Rochester`
- Faculty URL: `http://www.cs.rochester.edu/~lane`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues present.
- phd_score: `20`
- ra_score: `35`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.61`

### 459. Justin Thaler (Georgetown University)

- Rank: `86`
- Department: `Department of Computer Science`
- Faculty URL: `http://people.cs.georgetown.edu/jthaler`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues present.
- phd_score: `20`
- ra_score: `35`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.73`

### 460. Eugene Zhang (Oregon State University)

- Rank: `53`
- Department: `Electrical Engineering and Computer Science | College of Engineering`
- Faculty URL: `http://web.engr.oregonstate.edu/~zhange`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `20`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.49`

### 461. Greg Welch (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `https://sreal.ucf.edu/people/welch`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `20`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.49`

### 462. Alessandro Flammini (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `http://cnets.indiana.edu/aflammin`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `20`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.49`

### 463. Benjamin Raichel (University of Texas at Dallas)

- Rank: `55`
- Department: `UT Dallas SSO Login`
- Faculty URL: `http://www.utdallas.edu/~bar150630`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `20`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.61`

### 464. José A. B. Fortes (University of Florida)

- Rank: `59`
- Department: `Department of Computer & Information Science & Engineering`
- Faculty URL: `https://www.acis.ufl.edu/people/fortes`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `20`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.49`

### 465. Kai Shen (University of Rochester)

- Rank: `59`
- Department: `Department of Computer Science : University of Rochester`
- Faculty URL: `https://www.cs.rochester.edu/u/kshen`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `20`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.49`

### 466. Deeparnab Chakrabarty (Dartmouth College)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `http://web.cs.dartmouth.edu/people/deeparnab-chakrabarty`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `20`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.49`

### 467. Donald M. Chiarulli (University of Pittsburgh)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `https://people.cs.pitt.edu/~don`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `20`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.49`

### 468. Aaron D. Ames (California Inst. of Technology)

- Rank: `80`
- Department: `Computing + Mathematical Sciences`
- Faculty URL: `http://ames.caltech.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `20`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.61`

### 469. Richard M. Murray (California Inst. of Technology)

- Rank: `80`
- Department: `Computing + Mathematical Sciences`
- Faculty URL: `https://www.bbe.caltech.edu/people/richard-m-murray`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `20`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.49`

### 470. Venkat Chandrasekaran (California Inst. of Technology)

- Rank: `80`
- Department: `Computing + Mathematical Sciences`
- Faculty URL: `http://users.cms.caltech.edu/~venkatc`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `20`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.49`

### 471. John Murray-Bruce (University of South Florida)

- Rank: `80`
- Department: `Bellini College of Artificial Intelligence, Cybersecurity and Computing`
- Faculty URL: `https://www.cse.usf.edu/~murraybruce`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `20`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.49`

### 472. Lisa Singh (Georgetown University)

- Rank: `86`
- Department: `Department of Computer Science`
- Faculty URL: `http://people.cs.georgetown.edu/~singh`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `20`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.61`

### 473. Zheng Dong 0002 (Wayne State University)

- Rank: `86`
- Department: `Wayne State University`
- Faculty URL: `http://zheng.eng.wayne.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `20`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.61`

### 474. Sibel Adali (Rensselaer Polytechnic Institute)

- Rank: `89`
- Department: `Computer Science`
- Faculty URL: `http://www.cs.rpi.edu/~sibel/SibelAdali/Sibel_Adali.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `20`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.49`

### 475. Charles K. Nicholas (Univ. of Maryland - Baltimore County)

- Rank: `89`
- Department: `Department of Computer Science and Electrical Engineering – UMBC`
- Faculty URL: `http://www.csee.umbc.edu/~nicholas/charles_nicholas.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `20`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.61`

### 476. Vandana Pursnani Janeja (Univ. of Maryland - Baltimore County)

- Rank: `89`
- Department: `Department of Computer Science and Electrical Engineering – UMBC`
- Faculty URL: `https://userpages.umbc.edu/~vjaneja`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `20`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.61`

### 477. Indrakshi Ray (Colorado State University)

- Rank: `97`
- Department: `Department of Computer Science | CSU – Department of Computer Science at Colorado State University`
- Faculty URL: `http://www.cs.colostate.edu/~iray`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `20`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.49`

### 478. Mooi Choo Chuah (Lehigh University)

- Rank: `97`
- Department: `Computer Science & Engineering | P.C. Rossin College of Engineering & Applied Science`
- Faculty URL: `http://www.cse.lehigh.edu/~chuah`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `20`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.49`

### 479. Benyuan Liu (University of Massachusetts Lowell)

- Rank: `97`
- Department: `Miner School of Computer and Information Sciences | Kennedy College of Sciences | UMass Lowell`
- Faculty URL: `http://www.cs.uml.edu/~bliu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `20`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.61`

### 480. Lei Jiang 0001 (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `http://homes.sice.indiana.edu/jiang60`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues present.
- phd_score: `18`
- ra_score: `43`
- rationale_phd: Explicit overlap found in: general AI / ML.
- rationale_ra: Relevant overlap found in: general AI / ML. RA or recruiting cues are explicit.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 481. Amy Greenwald (Brown University)

- Rank: `52`
- Department: `Brown University Department of Computer Science`
- Faculty URL: `http://cs.brown.edu/~amygreen`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `18`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 482. Farokh B. Bastani (University of Texas at Dallas)

- Rank: `55`
- Department: `UT Dallas SSO Login`
- Faculty URL: `https://www.utdallas.edu/~bastani`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `18`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 483. Latifur Khan (University of Texas at Dallas)

- Rank: `55`
- Department: `UT Dallas SSO Login`
- Faculty URL: `https://www.utdallas.edu/~lkhan`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `18`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 484. Vibhav Gogate (University of Texas at Dallas)

- Rank: `55`
- Department: `UT Dallas SSO Login`
- Faculty URL: `https://personal.utdallas.edu/~vibhav.gogate/index.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `18`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 485. Yiyu Shi 0001 (University of Notre Dame)

- Rank: `59`
- Department: `Home - Computer Science and Engineering`
- Faculty URL: `https://engineering.nd.edu/faculty/yiyu-shi`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `18`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 486. Gautam Das 0001 (University of Texas at Arlington)

- Rank: `59`
- Department: `Computer Science and Engineering - The University of Texas at Arlington`
- Faculty URL: `http://ranger.uta.edu/~gdas`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `18`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 487. Song Han 0002 (University of Connecticut)

- Rank: `63`
- Department: `Home | School of Computing | College of Engineering`
- Faculty URL: `http://engr.uconn.edu/~song`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `18`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 488. Reuth Mirsky (Tufts University)

- Rank: `70`
- Department: `Homepage | Department of Computer Science`
- Faculty URL: `https://engineering.tufts.edu/cs/people/faculty/reuth-mirsky`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `18`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 489. K. Vijay-Shanker (University of Delaware)

- Rank: `70`
- Department: `Computer & Information Sciences at the University of Delaware`
- Faculty URL: `https://www.eecis.udel.edu/~vijay`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `18`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 490. Keith S. Decker (University of Delaware)

- Rank: `70`
- Department: `Computer & Information Sciences at the University of Delaware`
- Faculty URL: `https://www.eecis.udel.edu/~decker`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `18`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 491. Ali Jannesari (Iowa State University)

- Rank: `80`
- Department: `Department of Computer Science`
- Faculty URL: `https://www.cs.iastate.edu/swapp/people/ali-jannesari`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `18`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 492. Christopher J. Quinn (Iowa State University)

- Rank: `80`
- Department: `Department of Computer Science`
- Faculty URL: `https://www.cs.iastate.edu/people/christopher-quinn`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `18`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 493. Danyang Zhang (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `https://www.york.cuny.edu/portal_college/dzhang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `18`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 494. Rohit Parikh (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `http://www.sci.brooklyn.cuny.edu/cis/parikh`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `18`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 495. Subash Shankar (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `http://www.cs.hunter.cuny.edu/~sshankar`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `18`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 496. L. Darrell Whitley (Colorado State University)

- Rank: `97`
- Department: `Department of Computer Science | CSU – Department of Computer Science at Colorado State University`
- Faculty URL: `http://www.cs.colostate.edu/~whitley`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `18`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 497. Hector Muñoz-Avila (Lehigh University)

- Rank: `97`
- Department: `Computer Science & Engineering | P.C. Rossin College of Engineering & Applied Science`
- Faculty URL: `http://www.cse.lehigh.edu/~munoz`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `18`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 498. Hantao Zhang 0001 (University of Iowa)

- Rank: `97`
- Department: `Computer Science | College of Liberal Arts and Sciences | The University of Iowa`
- Faculty URL: `https://www.cs.uiowa.edu/~hzhang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `18`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 499. Berthe Y. Choueiry (University of Nebraska)

- Rank: `97`
- Department: `School of Computing | Nebraska`
- Faculty URL: `http://cse.unl.edu/~choueiry`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI / ML; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `18`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: general AI / ML.
- rationale_ra: Relevant overlap found in: general AI / ML.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 500. Pietro Perona (California Inst. of Technology)

- Rank: `80`
- Department: `Computing + Mathematical Sciences`
- Faculty URL: `https://www.vision.caltech.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computer vision; advising cues UNKNOWN; RA cues present.
- phd_score: `16`
- ra_score: `41`
- rationale_phd: Explicit overlap found in: computer vision.
- rationale_ra: Relevant overlap found in: computer vision. RA or recruiting cues are explicit.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 501. Clay Stevens (Iowa State University)

- Rank: `80`
- Department: `Department of Computer Science`
- Faculty URL: `https://www.cs.iastate.edu/people/clay-stevens`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `16`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 502. Nazli Goharian (Georgetown University)

- Rank: `86`
- Department: `Department of Computer Science`
- Faculty URL: `http://people.cs.georgetown.edu/~nazli`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in NLP / language models; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `16`
- ra_score: `18`
- rationale_phd: Explicit overlap found in: NLP / language models. Recent work cues are present.
- rationale_ra: Relevant overlap found in: NLP / language models. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.59`

### 503. Gabriel Taubin (Brown University)

- Rank: `52`
- Department: `Brown University Department of Computer Science`
- Faculty URL: `http://mesh.brown.edu/taubin`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in computer vision; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `16`
- ra_score: `16`
- rationale_phd: Explicit overlap found in: computer vision.
- rationale_ra: Relevant overlap found in: computer vision.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.47`

### 504. Yiying Tong (Michigan State University)

- Rank: `67`
- Department: `Computer Science and Engineering | College of Engineering`
- Faculty URL: `http://www.cse.msu.edu/~ytong`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `15`
- ra_score: `35`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Advising or prospective-student cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. RA or recruiting cues are explicit. Student-mentoring cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. Research fit evidence is sparse.
- confidence: `0.41`

### 505. Shi-Kuo Chang (University of Pittsburgh)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `https://cs.pitt.edu/~chang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `15`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Advising or prospective-student cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Student-mentoring cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page.
- confidence: `0.49`

### 506. Cindy Grimm (Oregon State University)

- Rank: `53`
- Department: `Electrical Engineering and Computer Science | College of Engineering`
- Faculty URL: `http://web.engr.oregonstate.edu/~grimmc`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `12`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.49`

### 507. Kien A. Hua (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `https://dsg.cs.ucf.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `12`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.49`

### 508. Christopher M. Brown (University of Rochester)

- Rank: `59`
- Department: `Department of Computer Science : University of Rochester`
- Faculty URL: `https://www.cs.rochester.edu/~brown/home_orig.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `12`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.37`

### 509. William T. Hallahan (Binghamton University)

- Rank: `70`
- Department: `School of Computing`
- Faculty URL: `https://www.binghamton.edu/computer-science/people/profile.html?id=whallahan`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `12`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.37`

### 510. Babak Hassibi (California Inst. of Technology)

- Rank: `80`
- Department: `Computing + Mathematical Sciences`
- Faculty URL: `https://www.babak.caltech.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `12`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.37`

### 511. Joel W. Burdick (California Inst. of Technology)

- Rank: `80`
- Department: `Computing + Mathematical Sciences`
- Faculty URL: `http://robotics.caltech.edu/wiki/index.php/Robotics`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `12`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.49`

### 512. John Licato (University of South Florida)

- Rank: `80`
- Department: `Bellini College of Artificial Intelligence, Cybersecurity and Computing`
- Faculty URL: `https://cse.usf.edu/~licato`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `12`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.37`

### 513. Saumya K. Debray (University of Arizona)

- Rank: `83`
- Department: `University of Arizona Department of Computer Science | Computer Science`
- Faculty URL: `https://www.cs.arizona.edu/~debray`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `12`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.37`

### 514. Brian Murphy (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `http://www.baruch.cuny.edu/wsas/academics/history/bmurphy.htm`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `12`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.37`

### 515. Ping Ji 0002 (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `http://jjcweb.jjay.cuny.edu/pji`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `12`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.37`

### 516. Stephen Huang (University of Houston)

- Rank: `97`
- Department: `University of Houston`
- Faculty URL: `http://www2.cs.uh.edu/shuang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `12`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.37`

### 517. Jun Li 0001 (University of Oregon)

- Rank: `97`
- Department: `Computer Science | School of Computer and Data Sciences`
- Faculty URL: `http://ix.cs.uoregon.edu/~lijun`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: Evidence shows overlap in general AI-adjacent evidence only; advising cues UNKNOWN; RA cues UNKNOWN.
- phd_score: `12`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Research description is explicit.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.37`

### 518. Yangming Li (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `https://people.rit.edu/ymliee`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `35`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.61`

### 519. Xuanyu Cao (Washington State University)

- Rank: `86`
- Department: `School of Electrical Engineering & Computer Science`
- Faculty URL: `https://labs.wsu.edu/xuanyu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `35`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. RA or recruiting cues are explicit. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.41`

### 520. Amir Nayyeri (Oregon State University)

- Rank: `53`
- Department: `Electrical Engineering and Computer Science | College of Engineering`
- Faculty URL: `https://web.engr.oregonstate.edu/~nayyeria`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 521. Annie S. Wu (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `http://www.cs.ucf.edu/~aswu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 522. Edith Hemaspaandra (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `https://www.cs.rit.edu/~eh`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 523. Matt Huenerfauth (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `http://huenerfauth.ist.rit.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 524. Mohan Kumar (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `https://www.cs.rit.edu/~mjk`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 525. Binbin Xie (University of Texas at Arlington)

- Rank: `59`
- Department: `Computer Science and Engineering - The University of Texas at Arlington`
- Faculty URL: `https://www.uta.edu/academics/faculty/profile?username=xieb`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 526. Bo Fang 0002 (University of Texas at Arlington)

- Rank: `59`
- Department: `Computer Science and Engineering - The University of Texas at Arlington`
- Faculty URL: `https://www.uta.edu/academics/faculty/profile?user=bo.fang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 527. Dajiang Zhu (University of Texas at Arlington)

- Rank: `59`
- Department: `Computer Science and Engineering - The University of Texas at Arlington`
- Faculty URL: `https://mentis.uta.edu/explore/profile/dajiang-zhu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 528. Farhad Kamangar (University of Texas at Arlington)

- Rank: `59`
- Department: `Computer Science and Engineering - The University of Texas at Arlington`
- Faculty URL: `http://ranger.uta.edu/~kamangar`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 529. Harry Shomer (University of Texas at Arlington)

- Rank: `59`
- Department: `Computer Science and Engineering - The University of Texas at Arlington`
- Faculty URL: `https://www.uta.edu/academics/faculty/profile?user=harry.shomer`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 530. Sihong He (University of Texas at Arlington)

- Rank: `59`
- Department: `Computer Science and Engineering - The University of Texas at Arlington`
- Faculty URL: `https://www.uta.edu/academics/faculty/profile?username=hes2`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 531. Marten van Dijk (University of Connecticut)

- Rank: `63`
- Department: `Home | School of Computing | College of Engineering`
- Faculty URL: `https://scl.engr.uconn.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 532. Douglas C. Schmidt (College of William and Mary)

- Rank: `67`
- Department: `Computer Science | School of Computing, Data Sciences & Physics | William & Mary`
- Faculty URL: `https://dcschmidt.pages.wm.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 533. Pieter Peers (College of William and Mary)

- Rank: `67`
- Department: `Computer Science | School of Computing, Data Sciences & Physics | William & Mary`
- Faculty URL: `http://www.cs.wm.edu/~ppeers`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 534. Abhishek Dubey (Vanderbilt University)

- Rank: `70`
- Department: `Department of Computer Science - School of EngineeringSchool of Engineering`
- Faculty URL: `https://engineering.vanderbilt.edu/bio/?pid=abhishek-dubey`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 535. Bennett A. Landman (Vanderbilt University)

- Rank: `70`
- Department: `Department of Computer Science - School of EngineeringSchool of Engineering`
- Faculty URL: `https://engineering.vanderbilt.edu/bio/?pid=bennett-landman`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 536. Bobby Bodenheimer (Vanderbilt University)

- Rank: `70`
- Department: `Department of Computer Science - School of EngineeringSchool of Engineering`
- Faculty URL: `https://engineering.vanderbilt.edu/bio/?pid=robert-bodenheimer`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 537. Daniel B. Work (Vanderbilt University)

- Rank: `70`
- Department: `Department of Computer Science - School of EngineeringSchool of Engineering`
- Faculty URL: `https://engineering.vanderbilt.edu/bio/daniel-work`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 538. Dario J. Englot (Vanderbilt University)

- Rank: `70`
- Department: `Department of Computer Science - School of EngineeringSchool of Engineering`
- Faculty URL: `https://www.vanderbilt.edu/vise/visepeople/dario-j-englot`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 539. Gautam Biswas (Vanderbilt University)

- Rank: `70`
- Department: `Department of Computer Science - School of EngineeringSchool of Engineering`
- Faculty URL: `https://engineering.vanderbilt.edu/bio/?pid=gautam-biswas`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 540. Ipek Oguz (Vanderbilt University)

- Rank: `70`
- Department: `Department of Computer Science - School of EngineeringSchool of Engineering`
- Faculty URL: `https://engineering.vanderbilt.edu/bio/?pid=ipek-oguz`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 541. Kevin Leach (Vanderbilt University)

- Rank: `70`
- Department: `Department of Computer Science - School of EngineeringSchool of Engineering`
- Faculty URL: `https://engineering.vanderbilt.edu/bio/?pid=kevin-leach`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 542. Matthew Berger (Vanderbilt University)

- Rank: `70`
- Department: `Department of Computer Science - School of EngineeringSchool of Engineering`
- Faculty URL: `https://engineering.vanderbilt.edu/bio/?pid=matthew-berger`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 543. Meiyi Ma (Vanderbilt University)

- Rank: `70`
- Department: `Department of Computer Science - School of EngineeringSchool of Engineering`
- Faculty URL: `https://engineering.vanderbilt.edu/bio/?pid=meiyi-ma`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 544. Xenofon D. Koutsoukos (Vanderbilt University)

- Rank: `70`
- Department: `Department of Computer Science - School of EngineeringSchool of Engineering`
- Faculty URL: `https://engineering.vanderbilt.edu/bio/?pid=xenofon-koutsoukos`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 545. Michael I. Mandel (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `http://www.brooklyn.cuny.edu/web/academics/faculty/faculty_profile.jsp?faculty=1264`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 546. Christopher W. Geib (Drexel University)

- Rank: `89`
- Department: `Computer Science Department | Drexel CCI`
- Faculty URL: `http://drexel.edu/cci/contact/Faculty/Geib-Christopher`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 547. Lynne E. Parker (University of Tennessee)

- Rank: `89`
- Department: `University of Tennessee`
- Faculty URL: `http://web.eecs.utk.edu/~leparker`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 548. Michael W. Berry (University of Tennessee)

- Rank: `89`
- Department: `University of Tennessee`
- Faculty URL: `http://web.eecs.utk.edu/~mberry`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.49`

### 549. Bogdan S. Chlebus (Augusta University)

- Rank: `97`
- Department: `School of Computer and Cyber Sciences`
- Faculty URL: `https://www.augusta.edu/faculty/directory/view.php?id=BCHLEBUS`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 550. Dariusz R. Kowalski (Augusta University)

- Rank: `97`
- Department: `School of Computer and Cyber Sciences`
- Faculty URL: `https://www.augusta.edu/faculty/directory/view.php?id=DKOWALSKI`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 551. Wei Zhang 0090 (Augusta University)

- Rank: `97`
- Department: `School of Computer and Cyber Sciences`
- Faculty URL: `https://www.augusta.edu/faculty/directory/view.php?id=WZHANG1`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 552. Michael Kirby (Colorado State University)

- Rank: `97`
- Department: `Department of Computer Science | CSU – Department of Computer Science at Colorado State University`
- Faculty URL: `https://www.math.colostate.edu/~kirby`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 553. Rakesh M. Verma (University of Houston)

- Rank: `97`
- Department: `University of Houston`
- Faculty URL: `http://www2.cs.uh.edu/~rmverma`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `8`
- ra_score: `10`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Recent work cues are present.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. Recent activity cues are present.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.29`

### 554. Matthew W. Hahn (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `https://hahnlab.sitehost.iu.edu`
- Lab URL: `https://hahnlab.sitehost.iu.edu`
- Source Type: `lab_page`
- Summary: UNKNOWN
- phd_score: `3`
- ra_score: `5`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence. Evidence includes a lab-oriented page.
- rationale_ra: Direct topical overlap is not explicit in the available evidence. The evidence comes from an active lab-style page.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse. Affiliation evidence relies on a lab page rather than a faculty profile.
- confidence: `0.12`

### 555. Michael L. Littman (Brown University)

- Rank: `52`
- Department: `Brown University Department of Computer Science`
- Faculty URL: `http://cs.brown.edu/~mlittman`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 556. Philip N. Klein (Brown University)

- Rank: `52`
- Department: `Brown University Department of Computer Science`
- Faculty URL: `http://cs.brown.edu/~pnk`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 557. Sorin Istrail (Brown University)

- Rank: `52`
- Department: `Brown University Department of Computer Science`
- Faculty URL: `http://www.brown.edu/Research/Istrail_Lab/sorin.php`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 558. Thomas Serre (Brown University)

- Rank: `52`
- Department: `Brown University Department of Computer Science`
- Faculty URL: `https://serre-lab.clps.brown.edu/person/thomas-serre`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 559. Ben Lee (Oregon State University)

- Rank: `53`
- Department: `Electrical Engineering and Computer Science | College of Engineering`
- Faculty URL: `http://web.engr.oregonstate.edu/~benl/Ben_Lee/Welcome.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 560. Aritra Dutta (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `https://www.cs.ucf.edu/person/aritra-dutta`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 561. Charles E. Hughes (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `http://www.cs.ucf.edu/~ceh`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 562. Jialin Liu 0003 (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `https://www.cs.ucf.edu/person/jialin-liu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 563. Ladislau Bölöni (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `http://www.cs.ucf.edu/~lboloni`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 564. Roger Azevedo (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `https://www.ist.ucf.edu/People/Roger-Azevedo`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 565. Ser-Nam Lim (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `https://www.cs.ucf.edu/person/ser-nam-lim`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 566. Shahana Ibrahim (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `https://www.cs.ucf.edu/person/shahana-ibrahim`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 567. Shibu Yooseph (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `http://www.cs.ucf.edu/~syooseph`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 568. Shruti Vyas (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `https://www.cs.ucf.edu/person/shruti-vyas`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 569. Wu Lin (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `https://www.cs.ucf.edu/person/wulin`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 570. Yue Wang 0068 (University of Central Florida)

- Rank: `53`
- Department: `Home | UCF Department of Computer Science`
- Faculty URL: `https://www.cs.ucf.edu/person/yue-wang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 571. Chenghong Wang (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `https://luddy.indiana.edu/contact/profile/index.html?Chenghong_Wang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 572. Christopher Raphael (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `https://www.soic.indiana.edu/all-people/profile.html?profile_id=279`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 573. David B. Leake (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `https://www.cs.indiana.edu/~leake`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 574. David Crandall (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `http://www.cs.indiana.edu/~djcran`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 575. Funda Ergün (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `http://homes.soic.indiana.edu/fergun`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 576. Haewoon Kwak (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `https://luddy.indiana.edu/contact/profile/index.html?Haewoon_Kwak`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 577. Haixu Tang (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `http://www.informatics.indiana.edu/hatang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 578. Lantao Liu (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `http://homes.sice.indiana.edu/lantao`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 579. Mohsen Heidari (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `https://luddy.indiana.edu/contact/profile/index.html?Mohsen_Heidari`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 580. Qin Zhang 0001 (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `http://homes.soic.indiana.edu/qzhangcs`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 581. Samantha M. W. Wood (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `https://luddy.indiana.edu/contact/profile/index.html?Samantha_Wood`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 582. Yuzhen Ye (Indiana University)

- Rank: `55`
- Department: `Computer Science`
- Faculty URL: `http://mendel.informatics.indiana.edu/~yye/lab`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 583. Ding-Zhu Du (University of Texas at Dallas)

- Rank: `55`
- Department: `UT Dallas SSO Login`
- Faculty URL: `http://www.utdallas.edu/~dxd056000`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 584. Feng Chen 0001 (University of Texas at Dallas)

- Rank: `55`
- Department: `UT Dallas SSO Login`
- Faculty URL: `https://personal.utdallas.edu/~fxc190007`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 585. I-Ling Yen (University of Texas at Dallas)

- Rank: `55`
- Department: `UT Dallas SSO Login`
- Faculty URL: `http://www.utdallas.edu/~ilyen`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.37`

### 586. Vincent Ng 0001 (University of Texas at Dallas)

- Rank: `55`
- Department: `UT Dallas SSO Login`
- Faculty URL: `http://www.hlt.utdallas.edu/~vince`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 587. Weili Wu 0001 (University of Texas at Dallas)

- Rank: `55`
- Department: `UT Dallas SSO Login`
- Faculty URL: `http://www.utdallas.edu/~weiliwu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 588. Anne R. Haake (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `https://www.rit.edu/gccis/anne-haake`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 589. Jessica D. Bayliss (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `https://www.rit.edu/gccis/igm/jessica-bayliss`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 590. Linwei Wang (Rochester Inst. of Technology)

- Rank: `57`
- Department: `Department of Computer Science | Golisano College of Computing and Information Sciences | RIT`
- Faculty URL: `https://www.rit.edu/gccis/linwei-wang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 591. Qinghua Liu (Washington University in St. Louis)

- Rank: `58`
- Department: `Home | WashU Computer Science & Engineering`
- Faculty URL: `https://engineering.washu.edu/faculty/Qinghua-Liu.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 592. Anand Rangarajan 0001 (University of Florida)

- Rank: `59`
- Department: `Department of Computer & Information Science & Engineering`
- Faculty URL: `https://www.cise.ufl.edu/~anand`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 593. Arunava Banerjee (University of Florida)

- Rank: `59`
- Department: `Department of Computer & Information Science & Engineering`
- Faculty URL: `https://www.cise.ufl.edu/~arunava`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 594. Baba C. Vemuri (University of Florida)

- Rank: `59`
- Department: `Department of Computer & Information Science & Engineering`
- Faculty URL: `https://www.cise.ufl.edu/~vemuri`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 595. Bonnie J. Dorr (University of Florida)

- Rank: `59`
- Department: `Department of Computer & Information Science & Engineering`
- Faculty URL: `https://www.cise.ufl.edu/~bonniejdorr`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 596. Christina Gardner-McCune (University of Florida)

- Rank: `59`
- Department: `Department of Computer & Information Science & Engineering`
- Faculty URL: `https://www.cise.ufl.edu/people/faculty/gmccune`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 597. Damon L. Woodard (University of Florida)

- Rank: `59`
- Department: `Department of Computer & Information Science & Engineering`
- Faculty URL: `https://www.ece.ufl.edu/user/1469`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 598. Eric D. Ragan (University of Florida)

- Rank: `59`
- Department: `Department of Computer & Information Science & Engineering`
- Faculty URL: `https://www.cise.ufl.edu/ragan-eric`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 599. Kristy Elizabeth Boyer (University of Florida)

- Rank: `59`
- Department: `Department of Computer & Information Science & Engineering`
- Faculty URL: `https://www.cise.ufl.edu/boyer-kristy`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 600. Shigang Chen (University of Florida)

- Rank: `59`
- Department: `Department of Computer & Information Science & Engineering`
- Faculty URL: `http://www.cise.ufl.edu/~sgchen`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 601. Adam Czajka (University of Notre Dame)

- Rank: `59`
- Department: `Home - Computer Science and Engineering`
- Faculty URL: `https://engineering.nd.edu/profiles/aczajka`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 602. Chaoli Wang 0001 (University of Notre Dame)

- Rank: `59`
- Department: `Home - Computer Science and Engineering`
- Faculty URL: `http://www3.nd.edu/~cwang11/about.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 603. Collin McMillan (University of Notre Dame)

- Rank: `59`
- Department: `Home - Computer Science and Engineering`
- Faculty URL: `http://www.cse.nd.edu/~cmc`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 604. Jane Cleland-Huang (University of Notre Dame)

- Rank: `59`
- Department: `Home - Computer Science and Engineering`
- Faculty URL: `https://engineering.nd.edu/profiles/jcleland-huang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 605. Kevin W. Bowyer (University of Notre Dame)

- Rank: `59`
- Department: `Home - Computer Science and Engineering`
- Faculty URL: `http://www3.nd.edu/~kwb`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 606. Ronald A. Metoyer (University of Notre Dame)

- Rank: `59`
- Department: `Home - Computer Science and Engineering`
- Faculty URL: `https://engineering.nd.edu/profiles/rmetoyer`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 607. Xiaobo Hu (University of Notre Dame)

- Rank: `59`
- Department: `Home - Computer Science and Engineering`
- Faculty URL: `http://www3.nd.edu/~shu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 608. Xiaobo Sharon Hu (University of Notre Dame)

- Rank: `59`
- Department: `Home - Computer Science and Engineering`
- Faculty URL: `http://www3.nd.edu/~shu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 609. Gaurav Sharma (University of Rochester)

- Rank: `59`
- Department: `Department of Computer Science : University of Rochester`
- Faculty URL: `https://hajim.rochester.edu/ece/sites/gsharma`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 610. Ji Liu 0002 (University of Rochester)

- Rank: `59`
- Department: `Department of Computer Science : University of Rochester`
- Faculty URL: `http://www.cs.rochester.edu/u/jliu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 611. Randal C. Nelson (University of Rochester)

- Rank: `59`
- Department: `Department of Computer Science : University of Rochester`
- Faculty URL: `https://www.cs.rochester.edu/~nelson`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 612. Chengkai Li 0001 (University of Texas at Arlington)

- Rank: `59`
- Department: `Computer Science and Engineering - The University of Texas at Arlington`
- Faculty URL: `http://ranger.uta.edu/~cli`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 613. Hong Jiang 0001 (University of Texas at Arlington)

- Rank: `59`
- Department: `Computer Science and Engineering - The University of Texas at Arlington`
- Faculty URL: `http://ranger.uta.edu/~jiang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 614. Vassilis Athitsos (University of Texas at Arlington)

- Rank: `59`
- Department: `Computer Science and Engineering - The University of Texas at Arlington`
- Faculty URL: `http://omega.uta.edu/~athitsos`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 615. Yu Lei 0001 (University of Texas at Arlington)

- Rank: `59`
- Department: `Computer Science and Engineering - The University of Texas at Arlington`
- Faculty URL: `http://ranger.uta.edu/~ylei`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 616. Frank Y. Shih (NJIT)

- Rank: `63`
- Department: `Home | Department of Computer Science`
- Faculty URL: `https://web.njit.edu/~shih`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 617. Guiling Wang (NJIT)

- Rank: `63`
- Department: `Home | Department of Computer Science`
- Faculty URL: `https://web.njit.edu/~gwang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 618. Usman Roshan (NJIT)

- Rank: `63`
- Department: `Home | Department of Computer Science`
- Faculty URL: `http://cs.njit.edu/usman`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 619. Zhi Wei 0001 (NJIT)

- Rank: `63`
- Department: `Home | Department of Computer Science`
- Faculty URL: `https://web.njit.edu/~zhiwei`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 620. Alexander Russell (University of Connecticut)

- Rank: `63`
- Department: `Home | School of Computing | College of Engineering`
- Faculty URL: `http://www.engr.uconn.edu/~acr`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.37`

### 621. Laurent D. Michel (University of Connecticut)

- Rank: `63`
- Department: `Home | School of Computing | College of Engineering`
- Faculty URL: `http://www.engr.uconn.edu/~ldm`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 622. Sanguthevar Rajasekaran (University of Connecticut)

- Rank: `63`
- Department: `Home | School of Computing | College of Engineering`
- Faculty URL: `http://www.engr.uconn.edu/~rajasek`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 623. Erin Walker (University of Pittsburgh)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `https://cs.pitt.edu/faculty/tenure-stream/erin-walker`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 624. Hassan A. Karimi (University of Pittsburgh)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `http://gis.sis.pitt.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 625. Kayhan Batmanghelich (University of Pittsburgh)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `https://kayhan.dbmi.pitt.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 626. Paul W. Munro (University of Pittsburgh)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `http://www.pitt.edu/~pwm`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 627. Stephen Lee (University of Pittsburgh)

- Rank: `63`
- Department: `Department of Computer Science`
- Faculty URL: `http://www.sci.pitt.edu/faculty-and-research/faculty-directory/stephen-lee`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 628. Zhenming Liu (College of William and Mary)

- Rank: `67`
- Department: `Computer Science | School of Computing, Data Sciences & Physics | William & Mary`
- Faculty URL: `http://www.wm.edu/as/computerscience/faculty/liu_zhenming.php`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 629. Zhenghao Zhang (Florida State University)

- Rank: `67`
- Department: `DEPARTMENT OF COMPUTER SCIENCE – College of Arts and Sciences`
- Faculty URL: `http://www.cs.fsu.edu/~zzhang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 630. Abdol-Hossein Esfahanian (Michigan State University)

- Rank: `67`
- Department: `Computer Science and Engineering | College of Engineering`
- Faculty URL: `http://www.cse.msu.edu/~esfahani`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 631. Eric Torng (Michigan State University)

- Rank: `67`
- Department: `Computer Science and Engineering | College of Engineering`
- Faculty URL: `http://www.cse.msu.edu/~torng`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 632. Wolfgang Banzhaf (Michigan State University)

- Rank: `67`
- Department: `Computer Science and Engineering | College of Engineering`
- Faculty URL: `http://research.msu.edu/tag/wolfgang-banzhaf`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 633. Jeremy Blackburn (Binghamton University)

- Rank: `70`
- Department: `School of Computing`
- Faculty URL: `https://www.binghamton.edu/computer-science/contact/profile.html?id=jblackbu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 634. Shiqi Zhang 0001 (Binghamton University)

- Rank: `70`
- Department: `School of Computing`
- Faculty URL: `https://www.binghamton.edu/computer-science/contact/profile.html?id=zhangs`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 635. Sujoy Sikdar (Binghamton University)

- Rank: `70`
- Department: `School of Computing`
- Faculty URL: `https://www.binghamton.edu/computer-science/contact/profile.html?id=ssikdar`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 636. Enrique Dunn (Stevens Institute of Technology)

- Rank: `70`
- Department: `Department of Computer Science | External Site (Under Construction)`
- Faculty URL: `https://www.cs.stevens.edu/~edunn`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 637. Philippos Mordohai (Stevens Institute of Technology)

- Rank: `70`
- Department: `Department of Computer Science | External Site (Under Construction)`
- Faculty URL: `http://www.cs.stevens.edu/~mordohai`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 638. Wendy Hui Wang (Stevens Institute of Technology)

- Rank: `70`
- Department: `Department of Computer Science | External Site (Under Construction)`
- Faculty URL: `http://www.cs.stevens.edu/~hwang4`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 639. Xueqing Liu 0001 (Stevens Institute of Technology)

- Rank: `70`
- Department: `Department of Computer Science | External Site (Under Construction)`
- Faculty URL: `https://www.cs.stevens.edu/~xliu127`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 640. Usman A. Khan (Tufts University)

- Rank: `70`
- Department: `Homepage | Department of Computer Science`
- Faculty URL: `https://engineering.tufts.edu/cs/people/faculty/usman-khan`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 641. Vladimir Podolskii 0001 (Tufts University)

- Rank: `70`
- Department: `Homepage | Department of Computer Science`
- Faculty URL: `https://facultyprofiles.tufts.edu/vladimir-podolskii`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 642. Ben Carterette (University of Delaware)

- Rank: `70`
- Department: `Computer & Information Sciences at the University of Delaware`
- Faculty URL: `http://ir.cis.udel.edu/~carteret`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 643. Christopher Rasmussen (University of Delaware)

- Rank: `70`
- Department: `Computer & Information Sciences at the University of Delaware`
- Faculty URL: `https://www.eecis.udel.edu/~cer`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 644. Hagit Shatkay (University of Delaware)

- Rank: `70`
- Department: `Computer & Information Sciences at the University of Delaware`
- Faculty URL: `https://www.eecis.udel.edu/~shatkay`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 645. Kathleen F. McCoy (University of Delaware)

- Rank: `70`
- Department: `Computer & Information Sciences at the University of Delaware`
- Faculty URL: `http://udel.edu/~mccoy`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 646. Mohammad Mahdi Khalili (University of Delaware)

- Rank: `70`
- Department: `Computer & Information Sciences at the University of Delaware`
- Faculty URL: `https://sites.udel.edu/khalili`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 647. Bradley A. Malin (Vanderbilt University)

- Rank: `70`
- Department: `Department of Computer Science - School of EngineeringSchool of Engineering`
- Faculty URL: `https://hiplab.mc.vanderbilt.edu/people/malin`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 648. Eric Patterson (Clemson University)

- Rank: `75`
- Department: `School of Computing`
- Faculty URL: `https://people.cs.clemson.edu/~ekp`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 649. James Wang (Clemson University)

- Rank: `75`
- Department: `School of Computing`
- Faculty URL: `https://people.cs.clemson.edu/~jzwang`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 650. Anni Li (UNC - Charlotte)

- Rank: `75`
- Department: `Homepage - College of Computing and Informatics`
- Faculty URL: `https://ece.charlotte.edu/directory/dr-anni-li-phd`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 651. Ran Zhang (UNC - Charlotte)

- Rank: `75`
- Department: `Homepage - College of Computing and Informatics`
- Faculty URL: `https://ece.charlotte.edu/directory/dr-ran-zhang-phd`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 652. Alberto Cerpa (Univ. of California - Merced)

- Rank: `75`
- Department: `Computer Science & Engineering (CSE) | School of Engineering`
- Faculty URL: `http://www.andes.ucmerced.edu/~acerpa`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 653. In Kee Kim (University of Georgia)

- Rank: `75`
- Department: `University of Georgia`
- Faculty URL: `https://cobweb.cs.uga.edu/~kim`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 654. Jaewoo Lee (University of Georgia)

- Rank: `75`
- Department: `University of Georgia`
- Faculty URL: `http://cobweb.cs.uga.edu/~jwlee`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 655. John A. Miller 0001 (University of Georgia)

- Rank: `75`
- Department: `University of Georgia`
- Faculty URL: `http://cobweb.cs.uga.edu/~jam`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 656. Krys J. Kochut (University of Georgia)

- Rank: `75`
- Department: `University of Georgia`
- Faculty URL: `http://cobweb.cs.uga.edu/~kochut`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 657. Kyu Hyung Lee (University of Georgia)

- Rank: `75`
- Department: `University of Georgia`
- Faculty URL: `http://cobweb.cs.uga.edu/~kyuhlee`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 658. Liming Cai (University of Georgia)

- Rank: `75`
- Department: `University of Georgia`
- Faculty URL: `http://cobweb.cs.uga.edu/~cai`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 659. Prashant Doshi (University of Georgia)

- Rank: `75`
- Department: `University of Georgia`
- Faculty URL: `http://thinc.cs.uga.edu/personnel.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 660. Shannon Quinn (University of Georgia)

- Rank: `75`
- Department: `University of Georgia`
- Faculty URL: `http://cobweb.cs.uga.edu/~squinn`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 661. Suchendra M. Bhandarkar (University of Georgia)

- Rank: `75`
- Department: `University of Georgia`
- Faculty URL: `http://cobweb.cs.uga.edu/~suchi`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 662. Tianming Liu 0001 (University of Georgia)

- Rank: `75`
- Department: `University of Georgia`
- Faculty URL: `http://cobweb.cs.uga.edu/~tliu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 663. Walter D. Potter (University of Georgia)

- Rank: `75`
- Department: `University of Georgia`
- Faculty URL: `http://cobweb.cs.uga.edu/~potter`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 664. Candace L. Sidner (Worcester Polytechnic Institute)

- Rank: `75`
- Department: `Computer Science`
- Faculty URL: `http://www.wpi.edu/academics/facultydir/cls.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 665. David C. Brown (Worcester Polytechnic Institute)

- Rank: `75`
- Department: `Computer Science`
- Faculty URL: `http://www.wpi.edu/academics/facultydir/dcb.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 666. Dmitry Korkin (Worcester Polytechnic Institute)

- Rank: `75`
- Department: `Computer Science`
- Faculty URL: `http://www.wpi.edu/academics/facultydir/dk2.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 667. Emmanuel Agu (Worcester Polytechnic Institute)

- Rank: `75`
- Department: `Computer Science`
- Faculty URL: `http://www.wpi.edu/academics/facultydir/eoa.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 668. Jacob Whitehill (Worcester Polytechnic Institute)

- Rank: `75`
- Department: `Computer Science`
- Faculty URL: `https://www.wpi.edu/academics/facultydir/200331.htm`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 669. Joseph E. Beck (Worcester Polytechnic Institute)

- Rank: `75`
- Department: `Computer Science`
- Faculty URL: `http://www.wpi.edu/academics/facultydir/jb7.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 670. Neil T. Heffernan (Worcester Polytechnic Institute)

- Rank: `75`
- Department: `Computer Science`
- Faculty URL: `http://www.wpi.edu/academics/facultydir/nth.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 671. Andrew Stuart (California Inst. of Technology)

- Rank: `80`
- Department: `Computing + Mathematical Sciences`
- Faculty URL: `http://stuart.caltech.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 672. Houman Owhadi (California Inst. of Technology)

- Rank: `80`
- Department: `Computing + Mathematical Sciences`
- Faculty URL: `http://users.cms.caltech.edu/~owhadi/index.htm`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 673. Peter Schröder (California Inst. of Technology)

- Rank: `80`
- Department: `Computing + Mathematical Sciences`
- Faculty URL: `https://users.cms.caltech.edu/~ps`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 674. Soon-Jo Chung (California Inst. of Technology)

- Rank: `80`
- Department: `Computing + Mathematical Sciences`
- Faculty URL: `http://aerospacerobotics.caltech.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.37`

### 675. Tracey Ho (California Inst. of Technology)

- Rank: `80`
- Department: `Computing + Mathematical Sciences`
- Faculty URL: `http://www.its.caltech.edu/~tho`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 676. Bowen Weng (Iowa State University)

- Rank: `80`
- Department: `Department of Computer Science`
- Faculty URL: `https://www.cs.iastate.edu/people/bowen-weng-0`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 677. Giora Slutzki (Iowa State University)

- Rank: `80`
- Department: `Department of Computer Science`
- Faculty URL: `http://www.cs.iastate.edu/~slutzki`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 678. Guang Song (Iowa State University)

- Rank: `80`
- Department: `Department of Computer Science`
- Faculty URL: `http://www.cs.iastate.edu/people/guang-song`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 679. Kristin Y. Rozier (Iowa State University)

- Rank: `80`
- Department: `Department of Computer Science`
- Faculty URL: `https://www.cs.iastate.edu/kyrozier`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 680. Samik Basu 0001 (Iowa State University)

- Rank: `80`
- Department: `Department of Computer Science`
- Faculty URL: `http://www.cs.iastate.edu/~sbasu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 681. Wei Le (Iowa State University)

- Rank: `80`
- Department: `Department of Computer Science`
- Faculty URL: `http://www.cs.iastate.edu/~weile`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 682. Shaun J. Canavan (University of South Florida)

- Rank: `80`
- Department: `Bellini College of Artificial Intelligence, Cybersecurity and Computing`
- Faculty URL: `http://www.cse.usf.edu/~scanavan`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 683. Lu Peng 0001 (Tulane University)

- Rank: `83`
- Department: `Computer Science | Tulane University School of Science and Engineering`
- Faculty URL: `https://cs.tulane.edu/~lpeng3`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 684. Nicholas Mattei (Tulane University)

- Rank: `83`
- Department: `Computer Science | Tulane University School of Science and Engineering`
- Faculty URL: `http://www2.tulane.edu/sse/cs/faculty/nicholas-mattei.cfm`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 685. Ramgopal R. Mettu (Tulane University)

- Rank: `83`
- Department: `Computer Science | Tulane University School of Science and Engineering`
- Faculty URL: `http://www2.tulane.edu/sse/cs/faculty/ramgopal-mettu.cfm`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 686. Zizhan Zheng (Tulane University)

- Rank: `83`
- Department: `Computer Science | Tulane University School of Science and Engineering`
- Faculty URL: `http://www2.tulane.edu/sse/cs/faculty/zizhan-zheng.cfm`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 687. Alon Efrat (University of Arizona)

- Rank: `83`
- Department: `University of Arizona Department of Computer Science | Computer Science`
- Faculty URL: `http://www.cs.arizona.edu/people/alon`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 688. Chris Gniady (University of Arizona)

- Rank: `83`
- Department: `University of Arizona Department of Computer Science | Computer Science`
- Faculty URL: `https://www.cs.arizona.edu/people/gniady`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 689. Jing Hua 0001 (Wayne State University)

- Rank: `86`
- Department: `Wayne State University`
- Faculty URL: `http://www.cs.wayne.edu/~jinghua`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 690. Ming Dong 0001 (Wayne State University)

- Rank: `86`
- Department: `Wayne State University`
- Faculty URL: `http://www.cs.wayne.edu/~mdong`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 691. Zichun Zhong (Wayne State University)

- Rank: `86`
- Department: `Wayne State University`
- Faculty URL: `http://www.cs.wayne.edu/zzhong`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 692. Bon K. Sy (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `https://www.gc.cuny.edu/Page-Elements/Academics-Research-Centers-Initiatives/Doctoral-Programs/Computer-Science/Faculty-Bios/Bon-K-Sy`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 693. Changhe Yuan (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `http://url.cs.qc.cuny.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 694. Elena Filatova (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `https://www.citytech.cuny.edu/faculty/EFilatova`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 695. Jun Li 0017 (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `https://phantom.cs.qc.cuny.edu/li`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 696. Katherine St. John (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `http://comet.lehman.cuny.edu/stjohn`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 697. Mayank Goswami 0001 (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `https://boole.cs.qc.cuny.edu/mgoswami`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 698. Michael E. Kress (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `http://www.gc.cuny.edu/Page-Elements/Academics-Research-Centers-Initiatives/Doctoral-Programs/Computer-Science/Faculty-Bios/Michael-E-Kress`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 699. Rivka Levitan (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `http://www.sci.brooklyn.cuny.edu/~levitan`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 700. Robert M. Haralick (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `http://www.gc.cuny.edu/Page-Elements/Academics-Research-Centers-Initiatives/Doctoral-Programs/Computer-Science/Faculty-Bios/Robert-M-Haralick`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 701. Saptarashmi Bandyopadhyay (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `https://www.gc.cuny.edu/people/saptarashmi-bandyopadhyay`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 702. Theodore Brown (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `https://www.gc.cuny.edu/Page-Elements/Academics-Research-Centers-Initiatives/Doctoral-Programs/Computer-Science/Faculty-Bios/Theodore-Brown`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 703. William Gregory Sakas (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `http://www.cs.hunter.cuny.edu/~sakas`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 704. Xiangdong Li (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `http://www.gc.cuny.edu/Page-Elements/Academics-Research-Centers-Initiatives/Doctoral-Programs/Computer-Science/Faculty-Bios/Xiangdong-Li`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 705. Xiaowen Zhang (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `http://www.csi.cuny.edu/faculty/ZHANG_XIAOWEN.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 706. Yingli Tian (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `http://www-ee.ccny.cuny.edu/wwwn/yltian/home.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 707. Zhigang Zhu 0001 (CUNY)

- Rank: `89`
- Department: `CUNY`
- Faculty URL: `http://www-cs.ccny.cuny.edu/~zhu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 708. Shu-Ching Chen (Florida International University)

- Rank: `89`
- Department: `Knight Foundation School of Computing and Information Sciences`
- Faculty URL: `https://www.cs.fiu.edu/~chens`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 709. Wei Zeng 0002 (Florida International University)

- Rank: `89`
- Department: `Knight Foundation School of Computing and Information Sciences`
- Faculty URL: `http://cis.fiu.edu/~wzeng`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 710. Boleslaw K. Szymanski (Rensselaer Polytechnic Institute)

- Rank: `89`
- Department: `Computer Science`
- Faculty URL: `http://www.cs.rpi.edu/~szymansk`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 711. Christopher Bystroff (Rensselaer Polytechnic Institute)

- Rank: `89`
- Department: `Computer Science`
- Faculty URL: `http://www.bioinfo.rpi.edu/bystrc`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 712. Elliot Anshelevich (Rensselaer Polytechnic Institute)

- Rank: `89`
- Department: `Computer Science`
- Faculty URL: `http://www.cs.rpi.edu/~eanshel`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 713. Malik Magdon-Ismail (Rensselaer Polytechnic Institute)

- Rank: `89`
- Department: `Computer Science`
- Faculty URL: `http://www.cs.rpi.edu/~magdon`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 714. Selmer Bringsjord (Rensselaer Polytechnic Institute)

- Rank: `89`
- Department: `Computer Science`
- Faculty URL: `http://www.cogsci.rpi.edu/pl/faculty-staff-cogsci/selmer-bringsjord`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 715. Sergei Nirenburg (Rensselaer Polytechnic Institute)

- Rank: `89`
- Department: `Computer Science`
- Faculty URL: `http://www.cogsci.rpi.edu/pl/faculty-staff-cogsci/nirenburg`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 716. Jinbo Xu (TTI Chicago)

- Rank: `89`
- Department: `TTI Chicago`
- Faculty URL: `http://ttic.uchicago.edu/~jinbo`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 717. Nathan Srebro (TTI Chicago)

- Rank: `89`
- Department: `TTI Chicago`
- Faculty URL: `http://ttic.uchicago.edu/~nati`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 718. Hongchang Gao (Temple University)

- Rank: `89`
- Department: `Department of Computer & Information Sciences | College of Science and Technology`
- Faculty URL: `https://www.cst.temple.edu/~tuo14379`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 719. Kai Zhang 0001 (Temple University)

- Rank: `89`
- Department: `Department of Computer & Information Sciences | College of Science and Technology`
- Faculty URL: `https://cis.temple.edu/user/635`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 720. Richard Beigel (Temple University)

- Rank: `89`
- Department: `Department of Computer & Information Sciences | College of Science and Technology`
- Faculty URL: `https://cis.temple.edu/~beigel`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 721. Xiaojiang Du (Temple University)

- Rank: `89`
- Department: `Department of Computer & Information Sciences | College of Science and Technology`
- Faculty URL: `https://cis.temple.edu/~xjdu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 722. Don Engel (Univ. of Maryland - Baltimore County)

- Rank: `89`
- Department: `Department of Computer Science and Electrical Engineering – UMBC`
- Faculty URL: `https://www.csee.umbc.edu/people/faculty/don-engel`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 723. Nirmalya Roy (Univ. of Maryland - Baltimore County)

- Rank: `89`
- Department: `Department of Computer Science and Electrical Engineering – UMBC`
- Faculty URL: `https://mpsc.umbc.edu/nroy`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page.
- confidence: `0.37`

### 724. Rajasekhar Anguluri (Univ. of Maryland - Baltimore County)

- Rank: `89`
- Department: `Department of Computer Science and Electrical Engineering – UMBC`
- Faculty URL: `https://www.csee.umbc.edu/rajasekhar-anguluri`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 725. Tim Oates 0001 (Univ. of Maryland - Baltimore County)

- Rank: `89`
- Department: `Department of Computer Science and Electrical Engineering – UMBC`
- Faculty URL: `http://www.csee.umbc.edu/people/faculty/tim-oates`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 726. Amir Sadovnik (University of Tennessee)

- Rank: `89`
- Department: `University of Tennessee`
- Faculty URL: `http://uvu.eecs.utk.edu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 727. Donatello Materassi (University of Tennessee)

- Rank: `89`
- Department: `University of Tennessee`
- Faculty URL: `http://www.eecs.utk.edu/people/faculty/dmateras`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 728. Jinyuan Sun (University of Tennessee)

- Rank: `89`
- Department: `University of Tennessee`
- Faculty URL: `http://web.eecs.utk.edu/~jysun`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 729. Mongi A. Abidi (University of Tennessee)

- Rank: `89`
- Department: `University of Tennessee`
- Faculty URL: `http://www.eecs.utk.edu/people/faculty/abidi`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 730. Charles W. Anderson (Colorado State University)

- Rank: `97`
- Department: `Department of Computer Science | CSU – Department of Computer Science at Colorado State University`
- Faculty URL: `http://www.cs.colostate.edu/~anderson`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 731. Xiuzhen Cheng 0001 (George Washington University)

- Rank: `97`
- Department: `Department of Computer Science | School of Engineering & Applied Science | The George Washington University`
- Faculty URL: `https://www.seas.gwu.edu/~cheng`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 732. Albert Mo Kim Cheng (University of Houston)

- Rank: `97`
- Department: `University of Houston`
- Faculty URL: `http://www2.cs.uh.edu/~acheng/acheng.html`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 733. Gopal Pandurangan (University of Houston)

- Rank: `97`
- Department: `University of Houston`
- Faculty URL: `http://www.uh.edu/nsm/computer-science/news-events/stories/2014/0711-pandurangan.php`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 734. Ioannis A. Kakadiaris (University of Houston)

- Rank: `97`
- Department: `University of Houston`
- Faculty URL: `http://cbl.uh.edu/pages/aboutcbl/dr_kakadiaris_biography`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 735. Ioannis T. Pavlidis (University of Houston)

- Rank: `97`
- Department: `University of Houston`
- Faculty URL: `http://www.cpl.uh.edu/people/ioannis_pavlidis`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 736. Ricardo Vilalta (University of Houston)

- Rank: `97`
- Department: `University of Houston`
- Faculty URL: `http://www2.cs.uh.edu/~vilalta`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 737. Weidong Shi (University of Houston)

- Rank: `97`
- Department: `University of Houston`
- Faculty URL: `http://www.uh.edu/nsm/computer-science/people/spotlight/spotlights/2014/larry-shi.php`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 738. Zhigang Deng 0001 (University of Houston)

- Rank: `97`
- Department: `University of Houston`
- Faculty URL: `http://graphics.cs.uh.edu/zdeng`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 739. Alberto M. Segre (University of Iowa)

- Rank: `97`
- Department: `Computer Science | College of Liberal Arts and Sciences | The University of Iowa`
- Faculty URL: `https://www.cs.uiowa.edu/people/alberto-maria-segre`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 740. Joe K. Kearney (University of Iowa)

- Rank: `97`
- Department: `Computer Science | College of Liberal Arts and Sciences | The University of Iowa`
- Faculty URL: `http://homepage.cs.uiowa.edu/~kearney`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 741. Jesse M. Heines (University of Massachusetts Lowell)

- Rank: `97`
- Department: `Miner School of Computer and Information Sciences | Kennedy College of Sciences | UMass Lowell`
- Faculty URL: `https://www.uml.edu/Research/IVPR/faculty/Heines_Jesse%20M.aspx`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 742. Tingjian Ge (University of Massachusetts Lowell)

- Rank: `97`
- Department: `Miner School of Computer and Information Sciences | Kennedy College of Sciences | UMass Lowell`
- Faculty URL: `http://www.cs.uml.edu/~ge`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 743. Yu Cao 0002 (University of Massachusetts Lowell)

- Rank: `97`
- Department: `Miner School of Computer and Information Sciences | Kennedy College of Sciences | UMass Lowell`
- Faculty URL: `https://www.uml.edu/Sciences/computer-science/faculty/Cao-Yu.aspx`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 744. Jitender S. Deogun (University of Nebraska)

- Rank: `97`
- Department: `School of Computing | Nebraska`
- Faculty URL: `http://cse.unl.edu/~deogun`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 745. Chenxi Qiu (University of North Texas)

- Rank: `97`
- Department: `Computer Science and Engineering`
- Faculty URL: `https://computerscience.engineering.unt.edu/people/faculty/chenxi-qiu`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 746. Mark V. Albert (University of North Texas)

- Rank: `97`
- Department: `Computer Science and Engineering`
- Faculty URL: `https://computerscience.engineering.unt.edu/people/faculty/mark-albert`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 747. Sanjukta Bhowmick (University of North Texas)

- Rank: `97`
- Department: `Computer Science and Engineering`
- Faculty URL: `https://computerscience.engineering.unt.edu/people/faculty/sanjukta-bhowmick`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 748. Serdar Bozdag (University of North Texas)

- Rank: `97`
- Department: `Computer Science and Engineering`
- Faculty URL: `https://computerscience.engineering.unt.edu/people/faculty/serdar-bozdag`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`

### 749. Allen D. Malony (University of Oregon)

- Rank: `97`
- Department: `Computer Science | School of Computer and Data Sciences`
- Faculty URL: `https://www.cs.uoregon.edu/People/Faculty/Allen_Malony.php`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.05`

### 750. Stephen Fickas (University of Oregon)

- Rank: `97`
- Department: `Computer Science | School of Computer and Data Sciences`
- Faculty URL: `http://ix.cs.uoregon.edu/~fickas`
- Lab URL: `UNKNOWN`
- Source Type: `faculty_page`
- Summary: UNKNOWN
- phd_score: `0`
- ra_score: `0`
- rationale_phd: No direct overlap with the user's target domains appears in the structured evidence.
- rationale_ra: Direct topical overlap is not explicit in the available evidence.
- potential_concerns: No explicit evidence of the user's highest-priority domains. No explicit RA / recruiting cue on the official evidence page. No explicit advising / prospective-student cue on the official evidence page. Research fit evidence is sparse.
- confidence: `0.17`
