from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def semantic_match(resume_text, job_desc):
    if not resume_text or not job_desc:
        return 0

    documents = [resume_text, job_desc]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    score = float(similarity[0][0]) * 100

    return round(score, 2)