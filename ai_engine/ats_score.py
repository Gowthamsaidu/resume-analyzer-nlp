def calculate_final_score(similarity_score, matched_skills, total_skills, section_scores):

    # Skill match percentage
    if total_skills == 0:
        skill_score = 0
    else:
        skill_score = (len(matched_skills) / total_skills) * 100

    # Section score total
    section_total = sum(section_scores.values())

    # Weighted ATS calculation
    final_score = (
        similarity_score * 0.4 +
        skill_score * 0.4 +
        section_total * 0.2
    )

    return round(final_score, 2)
