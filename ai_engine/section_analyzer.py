import re

def detect_sections(text):

    sections = {
        "skills": "",
        "projects": "",
        "experience": "",
        "education": ""
    }

    text_lower = text.lower()

    if "skills" in text_lower:
        sections["skills"] = "present"

    if "project" in text_lower:
        sections["projects"] = "present"

    if "experience" in text_lower or "internship" in text_lower:
        sections["experience"] = "present"

    if "education" in text_lower or "bachelor" in text_lower:
        sections["education"] = "present"

    return sections
