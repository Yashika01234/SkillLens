import streamlit as st
import pandas as pd
import plotly.express as px

from src.skilllens.matcher import analyze_match
from src.skilllens.skills import load_skill_catalog

st.set_page_config(page_title="SkillLens", page_icon="🔎", layout="wide")

st.markdown("""
<style>
.main {background-color: #fbfaff;}
.block-container {padding-top: 2rem; max-width: 1100px;}
.hero {padding: 1.5rem 1.8rem; border-radius: 18px; background: linear-gradient(120deg,#eeeaff,#f7f3ff);}
.hero h1 {margin: 0; color: #35256b;}
.hero p {color: #554b70; margin-bottom: 0;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>SkillLens</h1>
<p>Understand your resume-to-job fit. Find skill gaps. Plan your next step.</p>
</div>
""", unsafe_allow_html=True)

catalog = load_skill_catalog()
jobs = pd.read_csv("data/sample_jobs.csv")

with st.sidebar:
    st.header("Try a sample")
    selected_job = st.selectbox("Choose a sample job description", ["Custom"] + jobs["role"].tolist())
    if selected_job != "Custom":
        sample_description = jobs.loc[jobs["role"] == selected_job, "description"].iloc[0]
        st.caption("The selected sample will be inserted into the job description box.")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Your resume")
    resume_text = st.text_area(
        "Paste resume text",
        height=300,
        placeholder="Example: Electronics student with Python, C++, SQL, FastAPI, machine learning..."
    )
with col2:
    st.subheader("Target job")
    default_jd = sample_description if selected_job != "Custom" else ""
    job_text = st.text_area(
        "Paste job description",
        value=default_jd,
        height=300,
        placeholder="Paste the responsibilities and required skills from the job description..."
    )

if st.button("Analyse my match", type="primary", use_container_width=True):
    if not resume_text.strip() or not job_text.strip():
        st.warning("Please provide both your resume text and a job description.")
    else:
        result = analyze_match(resume_text, job_text, catalog)
        st.session_state["result"] = result

if "result" in st.session_state:
    result = st.session_state["result"]
    st.divider()
    st.subheader("Your analysis")

    score_col, skill_col, gap_col = st.columns(3)
    score_col.metric("Overall match", f'{result["match_score"]:.1f}%')
    skill_col.metric("Required skills found", len(result["matched_skills"]))
    gap_col.metric("Potential skill gaps", len(result["missing_skills"]))

    st.progress(min(result["match_score"] / 100, 1.0))
    st.caption("The score combines required-skill coverage (70%) and TF-IDF text similarity (30%). It is a comparison score, not a hiring probability.")

    left, right = st.columns(2)
    with left:
        st.markdown("#### Skills you have")
        if result["matched_skills"]:
            for skill in result["matched_skills"]:
                st.success(skill)
        else:
            st.info("No catalogued skills were detected in the resume text.")
    with right:
        st.markdown("#### Skills to consider developing")
        if result["missing_skills"]:
            for skill in result["missing_skills"]:
                st.warning(skill)
        else:
            st.success("All detected required skills appear in your resume.")

    st.markdown("#### Skill coverage")
    chart_data = pd.DataFrame({
        "Status": ["Found in resume", "Not found in resume"],
        "Count": [len(result["matched_skills"]), len(result["missing_skills"])]
    })
    fig = px.pie(chart_data, names="Status", values="Count", hole=0.55)
    fig.update_layout(margin=dict(t=10, b=10, l=10, r=10), legend_title_text="")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("#### Suggestions")
    for suggestion in result["suggestions"]:
        st.write(f"- {suggestion}")

    with st.expander("How was this score calculated?"):
        st.write(f'Skill coverage: {result["skill_coverage"]:.1f}%')
        st.write(f'TF-IDF text similarity: {result["text_similarity"]:.1f}%')
        st.write("Overall = 0.70 × skill coverage + 0.30 × text similarity.")
        st.write("Skill detection uses a transparent dictionary of common technical skills and aliases. Add more skills to data/skills.csv to expand it.")

st.divider()
st.caption("SkillLens is an educational NLP project. It does not predict hiring decisions and may miss skills that are phrased differently from its skill dictionary.")
