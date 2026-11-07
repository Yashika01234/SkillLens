                                                            <# SkillLens
                                                  ### ✦ Your Resume. Your Skills. Your Next Opportunity

<p align="center">
  An NLP-powered resume and job description matching assistant.
</p>

---

## ୨୧ About SkillLens

Finding the right skills for a job shouldn't feel like searching for a needle in a haystack.

**SkillLens** helps users understand how closely their resume matches a job description using Natural Language Processing (NLP).

Simply paste your resume and a job description to discover:
- Skills that match the job requirements.
- Skills that may be missing from your resume.
- An estimated resume-to-job matching score.
- Suggestions to improve your skill alignment.

## ✨ Features

| Feature | Description |
|---|---|
| Resume Analysis | Analyse resume text |
| Job Matching | Compare resumes with job descriptions |
| Skill Extraction | Identify technical skills automatically |
| Skill Gap Analysis | Highlight missing skills |
| Match Score | Calculate textual alignment |
| Visual Dashboard | Explore results through interactive charts |

## 🧠 How It Works

```text
       Resume + Job Description
                 |
                 v
          Text Processing
                 |
                 v
           Skill Extraction
                 |
                 v
          TF-IDF Vectorization
                 |
                 v
          Cosine Similarity
                 |
                 v
          Skill Gap Analysis
                 |
                 v
           Match Dashboard
```

## ⚙️ Tech Stack

- **Python** — Core development
- **Pandas** — Data processing
- **Scikit-learn** — NLP and text similarity
- **TF-IDF** — Text representation
- **Cosine Similarity** — Text comparison
- **Streamlit** — Interactive dashboard
- **Plotly** — Data visualization
- **Pytest** — Unit testing

## 📂 Project Structure

```text
SkillLens/
│
├── app.py
├── data/
│   ├── skills.csv
│   └── sample_jobs.csv
│
├── src/
│   └── skilllens/
│       ├── skills.py
│       └── matcher.py
│
├── tests/
│   └── test_matcher.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Yashika01234/SkillLens.git
cd SkillLens
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run SkillLens

```bash
streamlit run app.py
```

### 6. Run tests

```bash
pytest -q
```

## 📊 Matching Methodology

SkillLens combines two measurements:

- **Skill Coverage (70%)** — Percentage of detected job-required skills found in the resume.
- **Text Similarity (30%)** — TF-IDF cosine similarity between the resume and job description.

Overall Match Score:

`0.70 × Skill Coverage + 0.30 × Text Similarity`

The score is a heuristic measure of textual alignment, not a probability of getting hired.

## 🌱 Future Enhancements

- PDF and DOCX resume uploads.
- Expanded skill dictionary and synonym detection.
- Semantic similarity using sentence embeddings.
- Downloadable resume analysis reports.
- Improved skill recommendations.
- Resume analysis history.

## ⚠️ Disclaimer

SkillLens is an educational NLP project. Its matching score is not a measure of actual candidate ability or a prediction of recruitment outcomes. Skill detection depends on the available skill dictionary.

---

<p align="center">
  Made with curiosity and code.
  <br/><br/>
  **Yashika Nanda**
  <br/>
  <sub>Building smarter ways to understand skills and opportunities.</sub>
</p>
