# SkillLens
### Resume-to-Job Description Matching with Beginner-Friendly NLP

SkillLens is an educational NLP application that compares resume text with a job description. It highlights skills found in both documents, identifies potential skill gaps, and calculates an explainable text-alignment score.

## Features
- Resume and job description text input
- Skill extraction using a small, editable skill dictionary
- TF-IDF text vectorization
- Cosine similarity
- Required-skill coverage and missing-skill analysis
- Interactive Streamlit dashboard
- Sample job descriptions
- Unit tests with pytest

## How the score works
SkillLens combines two signals:

- 70% required-skill coverage: matched required skills divided by all detected required skills.
- 30% TF-IDF cosine similarity: similarity between the complete resume and job-description text.

`Overall score = 0.70 × skill coverage + 0.30 × text similarity`

This is a heuristic matching score, not a trained hiring model or probability of getting hired. The weights are design choices and have not been validated against recruiter decisions.

## Tech stack
Python, Pandas, Scikit-learn, Streamlit, Plotly, Pytest.

## Project structure
```text
SkillLens/
├── app.py
├── data/
│   ├── skills.csv
│   └── sample_jobs.csv
├── src/skilllens/
│   ├── __init__.py
│   ├── skills.py
│   └── matcher.py
├── tests/
│   └── test_matcher.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Run locally
```bash
git clone https://github.com/YOUR_USERNAME/SkillLens.git
cd SkillLens
python -m venv .venv
```

Windows:
```bash
.venv\\Scripts\\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install dependencies and launch:
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Run tests
```bash
pytest -q
```

## Limitations
- Skill extraction depends on the included dictionary and may miss synonyms, context, or skills not listed in `data/skills.csv`.
- TF-IDF and cosine similarity measure textual overlap, not a person's actual ability.
- The score is an explainable heuristic, not a probability of selection.
- Users should only list skills they can honestly demonstrate.

## Future improvements
- Expand skill taxonomy and add domain-specific synonyms.
- Add PDF/DOCX resume upload and text extraction.
- Add semantic embeddings to recognize related phrases.
- Add saved analysis history and exportable reports.
- Evaluate score quality using a manually reviewed set of resume/job pairs.

## Author
Yashika Nanda

*Built as a learning project to explore NLP, information retrieval, Python application development, and explainable matching.*
