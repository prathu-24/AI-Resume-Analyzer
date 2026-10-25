# 📄 AI Resume Analyzer

An interactive resume analysis web application built using Python and Streamlit. It extracts information from PDF resumes, identifies skills, checks compatibility with selected job roles, and provides suggestions for improvement.

## 🚀 Features

- **PDF Resume Upload:** Upload a resume in PDF format.
- **Contact Extraction:** Extract email addresses and phone numbers.
- **Skill Detection:** Identify technical and soft skills from resumes.
- **ATS Compatibility Score:** Calculate a skill-matching score for the selected job role.
- **Missing Skills Analysis:** Identify skills required for a role that are not detected in the resume.
- **Interactive Dashboard:** Display resume metrics and skill charts.
- **Resume Suggestions:** Recommend skills to improve job-role compatibility.
- **Extracted Text Preview:** View the text extracted from the uploaded resume.

## 🛠️ Technologies Used

- Python
- Streamlit
- PyPDF2
- Pandas
- Matplotlib
- Regular Expressions (Regex)
- Counter from Python's Collections module

## 💼 Supported Job Roles

- Data Scientist
- Web Developer
- AI Engineer

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository URL.

### 2. Navigate to the project folder

```bash
cd "AI Resume Analyzer"
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

## 📊 How It Works

1. Select a job role.
2. Upload a resume in PDF format.
3. Extract resume text and contact details.
4. Detect skills using keyword matching.
5. Compare detected skills with the selected role's required skills.
6. Display the compatibility score, missing skills, and suggestions.

## ⚠️ Important Note

The ATS score is a basic skill-matching percentage, not an official score from an Applicant Tracking System. Skill detection depends on keywords and may miss skills expressed using different wording. The application provides informational suggestions and does not guarantee recruitment outcomes.

## 🔮 Future Enhancements

- Use NLP models for more accurate skill extraction.
- Support DOCX resumes.
- Add job-description matching.
- Provide downloadable analysis reports.
- Improve skill matching using synonyms and semantic similarity.

## 👨‍💻 Project

**AI Resume Analyzer** — Resume analysis and job-role skill matching using Python.
