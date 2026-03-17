def find_missing_skills(resume_skills, job_skills):

    resume_set = set([s.lower() for s in resume_skills])
    job_set = set([s.lower() for s in job_skills])

    missing = list(job_set - resume_set)

    return missing
