import re

# Sample ICD-10 code map (add more for realism)
ICD10_MAP = {
    "E11.9": "Type 2 diabetes mellitus without complications",
    "I10": "Essential (primary) hypertension",
    "J45.909": "Unspecified asthma, uncomplicated",
    "F41.1": "Generalized anxiety disorder",
    "E78.5": "Hyperlipidemia, unspecified",
}

def extract_icd_codes(text: str) -> list:
    found_codes = []
    text_lower = text.lower()

    for code, desc in ICD10_MAP.items():
        # Check if the description or key terms are in the transcript
        keywords = desc.lower().split(",")[0].split(" ")
        if any(word in text_lower for word in keywords):
            found_codes.append(code)
    
    return found_codes
