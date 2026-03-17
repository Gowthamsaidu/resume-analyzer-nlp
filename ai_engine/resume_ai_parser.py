import spacy
import pdfplumber
import re

from sympy import python

nlp = spacy.load("en_core_web_sm")


# -------- Extract Text From PDF -------- #
def extract_text_from_pdf(file_path):

    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + " "

    return clean_text(text)


# -------- Clean Resume Text -------- #
def clean_text(text):

    text = text.lower()

    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    return text


# -------- Extract Skills -------- #
def extract_skills(text, skills_db):

    text = text.lower()

    found_skills = []

    for skill in skills_db:
        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))

def extract_resume_skills(resume_text, job_skills):

    found = []

    text = resume_text.lower()

    for skill in job_skills:

        if skill.lower() in text:
            found.append(skill)

    return list(set(found))

