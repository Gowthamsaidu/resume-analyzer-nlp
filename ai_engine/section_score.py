def calculate_section_scores(sections):

    scores = {}

    scores["skills_score"] = 25 if sections["skills"] else 0
    scores["projects_score"] = 25 if sections["projects"] else 0
    scores["experience_score"] = 25 if sections["experience"] else 0
    scores["education_score"] = 25 if sections["education"] else 0

    return scores
