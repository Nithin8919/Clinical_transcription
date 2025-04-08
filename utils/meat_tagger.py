import re

# Example keywords for MEAT criteria
MEAT_KEYWORDS = {
    "Monitoring": ["monitor", "follow-up", "observe", "review", "check"],
    "Evaluation": ["evaluate", "test", "screen", "assess", "measure"],
    "Assessment": ["diagnose", "symptom", "complain", "findings", "examination"],
    "Treatment": ["prescribe", "administer", "therapy", "recommend", "medication", "procedure"]
}

def tag_meat_compliance(transcript: str, icd_codes: list) -> dict:
    transcript_lower = transcript.lower()
    icd_meat_map = {}

    for code in icd_codes:
        meat_tags = []
        for category, keywords in MEAT_KEYWORDS.items():
            if any(re.search(rf"\b{kw}\b", transcript_lower) for kw in keywords):
                meat_tags.append(category)
        icd_meat_map[code] = meat_tags if meat_tags else ["No MEAT found"]
    
    return icd_meat_map
