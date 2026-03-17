def generate_suggestions(missing_skills):

    suggestions = []

    for skill in missing_skills:

        if "aws" in skill:
            suggestions.append("Add experience with AWS cloud services")

        elif "system design" in skill:
            suggestions.append("Mention system design knowledge in projects")

        elif "rest api" in skill:
            suggestions.append("Include REST API development experience")

        elif "microservices" in skill:
            suggestions.append("Add microservices architecture experience")

        elif "sql" in skill:
            suggestions.append("Highlight SQL or database projects")

        elif "python" in skill:
            suggestions.append("Add Python based projects")

        else:
            suggestions.append(f"Consider adding experience with {skill}")

    return suggestions[:5]
