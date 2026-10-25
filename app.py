import streamlit as st
import PyPDF2
import re
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
    color: white;
}

h1, h2, h3, h4 {
    color: white;
}

.block {
    background-color: #1E1E1E;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 15px;
    border: 1px solid #333;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.title("📄 AI Resume Analyzer")

st.write(
    "Analyze resumes using Artificial Intelligence and NLP."
)

# ---------------- JOB ROLES ---------------- #

job_roles = {

    "Data Scientist": [
        "python",
        "machine learning",
        "data science",
        "sql",
        "nlp"
    ],

    "Web Developer": [
        "html",
        "css",
        "javascript",
        "python"
    ],

    "AI Engineer": [
        "python",
        "deep learning",
        "tensorflow",
        "machine learning",
        "nlp"
    ]
}

# ---------------- ROLE SELECTOR ---------------- #

selected_role = st.selectbox(
    "🎯 Select Job Role",
    list(job_roles.keys())
)

required_skills = job_roles[selected_role]

# ---------------- SKILLS DATABASE ---------------- #

skills_db = [
    "python",
    "java",
    "c",
    "c++",
    "machine learning",
    "deep learning",
    "nlp",
    "data science",
    "sql",
    "html",
    "css",
    "javascript",
    "streamlit",
    "tensorflow",
    "pandas",
    "numpy",
    "communication",
    "leadership",
    "problem solving"
]

# ---------------- FILE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "📤 Upload Resume PDF",
    type=["pdf"]
)

# ---------------- PDF TEXT EXTRACTION ---------------- #

def extract_text_from_pdf(pdf_file):

    text = ""

    pdf_reader = PyPDF2.PdfReader(pdf_file)

    for page in pdf_reader.pages:

        text += page.extract_text()

    return text

# ---------------- MAIN PROCESS ---------------- #

if uploaded_file is not None:

    st.success("✅ Resume Uploaded Successfully!")

    # Extract text

    resume_text = extract_text_from_pdf(uploaded_file)

    resume_lower = resume_text.lower()

    # ==================================================
    # EMAIL EXTRACTION
    # ==================================================

    email = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",
        resume_text
    )

    # ==================================================
    # PHONE EXTRACTION
    # ==================================================

    phone = re.findall(
        r"\+?\d[\d -]{8,12}\d",
        resume_text
    )

    # ==================================================
    # SKILL DETECTION
    # ==================================================

    found_skills = []

    for skill in skills_db:

        if skill in resume_lower:

            found_skills.append(skill)

    # Remove duplicates

    found_skills = list(set(found_skills))

    # ==================================================
    # MISSING SKILLS
    # ==================================================

    missing_skills = []

    for skill in required_skills:

        if skill not in found_skills:

            missing_skills.append(skill)

    # ==================================================
    # ATS SCORE
    # ==================================================

    matched_skills = len(required_skills) - len(missing_skills)

    score = int(
        (matched_skills / len(required_skills)) * 100
    )

    # ==================================================
    # DASHBOARD METRICS
    # ==================================================

    st.markdown("---")

    st.header("📊 Resume Analysis Dashboard")

    m1, m2, m3, m4 = st.columns(4)

    m1.metric("Skills Found", len(found_skills))
    m2.metric("Missing Skills", len(missing_skills))
    m3.metric("ATS Score", f"{score}%")
    m4.metric("Selected Role", selected_role)

    st.markdown("---")

    # ==================================================
    # ATS SCORE BAR
    # ==================================================

    st.subheader("📈 ATS Compatibility Score")

    st.progress(score / 100)

    if score >= 80:

        st.success("Excellent Resume ⭐")

    elif score >= 50:

        st.warning("Good Resume but can improve 👍")

    else:

        st.error("Resume needs improvement ❌")

    st.markdown("---")

    # ==================================================
    # CONTACT DETAILS
    # ==================================================

    st.subheader("📧 Extracted Email")

    if email:

        st.success(email[0])

    else:

        st.error("No Email Found")

    st.subheader("📱 Extracted Phone Number")

    if phone:

        st.success(phone[0])

    else:

        st.error("No Phone Number Found")

    st.markdown("---")

    # ==================================================
    # DETECTED SKILLS
    # ==================================================

    st.subheader("✅ Detected Skills")

    if found_skills:

        skill_cols = st.columns(3)

        for index, skill in enumerate(found_skills):

            skill_cols[index % 3].success(skill)

    else:

        st.warning("No skills detected")

    st.markdown("---")

    # ==================================================
    # SKILL CHART
    # ==================================================

    st.subheader("📊 Skill Frequency Analysis")

    skill_counts = Counter(found_skills)

    chart_data = pd.DataFrame(
        skill_counts.items(),
        columns=["Skill", "Count"]
    )

    st.bar_chart(
        chart_data.set_index("Skill")
    )

    st.markdown("---")

    # ==================================================
    # MISSING SKILLS
    # ==================================================

    st.subheader("❌ Missing Skills")

    if missing_skills:

        for skill in missing_skills:

            st.error(skill)

    else:

        st.success("No missing skills")

    st.markdown("---")

    # ==================================================
    # AI SUGGESTIONS
    # ==================================================

    st.subheader("💡 AI Resume Suggestions")

    if missing_skills:

        for skill in missing_skills:

            st.info(
                f"Add '{skill}' to improve your ATS score."
            )

    else:

        st.success(
            "Your resume matches the selected role very well."
        )

    st.markdown("---")

   
    # ==================================================
    # EXTRACTED RESUME TEXT
    # ==================================================

    st.subheader("📄 Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=300
    )

# ---------------- FOOTER ---------------- #

st.markdown("---")

st.markdown(
    """
    <center>
    Developed using Python, Streamlit, NLP, PyPDF2 and AI-based Resume Analytics
    </center>
    """,
    unsafe_allow_html=True
)