from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.skilllens.skills import extract_skills


def calculate_text_similarity(resume_text, job_text):
    """Convert both texts to TF-IDF vectors and compare them with cosine similarity."""
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform([resume_text, job_text])
    score = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
    return float(score)


def analyze_match(resume_text, job_text, catalog):
    """Create a transparent resume/job comparison result."""
    resume_skills = set(extract_skills(resume_text, catalog))
    required_skills = set(extract_skills(job_text, catalog))

    matched = sorted(resume_skills.intersection(required_skills))
    missing = sorted(required_skills.difference(resume_skills))

    if required_skills:
        skill_coverage = len(matched) / len(required_skills)
    else:
        skill_coverage = 0.0

    text_similarity = calculate_text_similarity(resume_text, job_text)
    match_score = (0.70 * skill_coverage + 0.30 * text_similarity) * 100

    suggestions = []
    if missing:
        suggestions.append(
            "Review the missing skills and learn the ones that genuinely match your career goals."
        )
        suggestions.append(
            "If you already have experience with a missing skill, make that experience clearer in your resume."
        )
    else:
        suggestions.append(
            "Your resume contains all skills detected by the current skill dictionary for this job description."
        )
    suggestions.append(
        "Use specific evidence such as projects, coursework, internships, or measurable outcomes to support each skill."
    )

    return {
        "match_score": match_score,
        "skill_coverage": skill_coverage * 100,
        "text_similarity": text_similarity * 100,
        "resume_skills": sorted(resume_skills),
        "required_skills": sorted(required_skills),
        "matched_skills": matched,
        "missing_skills": missing,
        "suggestions": suggestions,
    }
