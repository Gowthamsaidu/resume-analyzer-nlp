from flask import Flask, render_template, request, redirect, session, jsonify
import os

# -------- AI ENGINE IMPORTS -------- #
from ai_engine.resume_ai_parser import extract_text_from_pdf, extract_resume_skills
from ai_engine.semantic_match import semantic_match
from ai_engine.skill_gap import find_missing_skills
from ai_engine.section_analyzer import detect_sections
from ai_engine.section_score import calculate_section_scores
from ai_engine.ats_score import calculate_final_score
from ai_engine.suggestions import generate_suggestions

# Company requirements
from companies import companies


app = Flask(__name__)
app.secret_key = "secret123"

users = {}

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# -------- HOME -------- #
@app.route("/")
def home():
    return render_template("login.html")


# -------- SIGNUP PAGE -------- #
@app.route("/signup")
def signup_page():
    return render_template("signup.html")


# -------- SIGNUP -------- #
@app.route("/signup", methods=["POST"])
def signup():

    username = request.form.get("username")
    password = request.form.get("password")

    if username in users:
        return "User already exists!"

    users[username] = password

    return redirect("/")


# -------- LOGIN -------- #
@app.route("/login", methods=["POST"])
def login():

    username = request.form.get("username")
    password = request.form.get("password")

    if username not in users or users[username] != password:
        return "Invalid credentials!"

    session["user"] = username

    return redirect("/dashboard")


# -------- DASHBOARD -------- #
@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/")

    return render_template(
        "dashboard.html",
        companies=list(companies.keys())
    )


# -------- LOGOUT -------- #
@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect("/")


# -------- ANALYZE RESUME -------- #
@app.route("/analyze", methods=["POST"])
def analyze():

    if "user" not in session:
        return jsonify({"error": "Unauthorized"})


    file = request.files.get("resume")
    company = request.form.get("company")

    if not file:
        return jsonify({"error": "No file uploaded"})


    # Save resume
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)


    # -------- Extract Resume Text -------- #
    resume_text = extract_text_from_pdf(filepath)


    # -------- Get Company Requirements -------- #
    company_data = companies.get(company, {})

    job_desc = company_data.get("description", "")
    job_skills = company_data.get("skills", [])


    # -------- Semantic Similarity -------- #
    similarity_score = semantic_match(resume_text, job_desc)


    # -------- Skill Extraction -------- #
    matched_skills = extract_resume_skills(resume_text, job_skills)


    # -------- Missing Skills -------- #
    missing_skills = find_missing_skills(matched_skills, job_skills)


    # -------- Resume Section Detection -------- #
    sections = detect_sections(resume_text)

    section_scores = calculate_section_scores(sections)


    # -------- Final ATS Score -------- #
    ats_score = calculate_final_score(
        similarity_score,
        matched_skills,
        len(job_skills),
        section_scores
    )


    # -------- AI Suggestions -------- #
    suggestions = generate_suggestions(missing_skills)


    return jsonify({
        "score": ats_score,
        "missing_skills": missing_skills[:10],
        "suggestions": suggestions,
        "sections": section_scores
    })


if __name__ == "__main__":
    app.run(debug=True)
