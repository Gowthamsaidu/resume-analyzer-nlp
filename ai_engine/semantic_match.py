from sentence_transformers import SentenceTransformer, util

# Load AI model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_match(resume_text, job_desc):

    if not resume_text or not job_desc:
        return 0

    # Convert text into embeddings
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_embedding = model.encode(job_desc, convert_to_tensor=True)

    # Cosine similarity
    similarity = util.cos_sim(resume_embedding, job_embedding)

    score = float(similarity[0][0]) * 100

    return round(score, 2)