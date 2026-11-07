from src.skilllens.matcher import analyze_match, calculate_text_similarity
from src.skilllens.skills import extract_skills


CATALOG = {
    "Python": ["python 3"],
    "SQL": [],
    "Machine Learning": ["ml"],
    "FastAPI": [],
}


def test_extract_skills_finds_aliases():
    found = extract_skills("I use Python 3 and ML.", CATALOG)
    assert found == ["Machine Learning", "Python"]


def test_extract_skills_avoids_partial_word_match():
    found = extract_skills("I know Flasking but not Flask.", {"Flask": []})
    assert found == ["Flask"]


def test_similarity_is_between_zero_and_one():
    score = calculate_text_similarity("Python developer", "Python developer role")
    assert 0 <= score <= 1


def test_matcher_finds_missing_skills():
    result = analyze_match(
        "Python developer with SQL experience",
        "Role requires Python, SQL and FastAPI",
        CATALOG,
    )
    assert result["matched_skills"] == ["Python", "SQL"]
    assert result["missing_skills"] == ["FastAPI"]
    assert 0 <= result["match_score"] <= 100


def test_no_detected_required_skills_does_not_crash():
    result = analyze_match("I enjoy teamwork", "Looking for a curious person", CATALOG)
    assert result["required_skills"] == []
    assert result["skill_coverage"] == 0
