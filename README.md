# 📄 AI Resume Analyzer

An interactive web application built using Python and Streamlit that analyzes PDF resumes, extracts contact information, identifies skills, calculates job-role skill compatibility, and provides suggestions to improve resumes.

## 🚀 Features

- **PDF Resume Upload:** Upload resumes in PDF format.
- **Email Extraction:** Automatically detect email addresses.
- **Phone Number Extraction:** Identify phone numbers from resume text.
- **Skill Detection:** Find technical and soft skills using keyword matching.
- **ATS Compatibility Score:** Calculate a skill-matching percentage for a selected job role.
- **Missing Skills Analysis:** Identify skills that may need improvement.
- **Interactive Dashboard:** Display resume metrics and visualizations.
- **Skill Frequency Chart:** Visualize detected skills using Streamlit charts.
- **Resume Suggestions:** Recommend skills related to the selected job role.
- **Extracted Text Preview:** View the text extracted from the uploaded PDF.

## 🛠️ Technologies Used

- Python
- Streamlit
- PyPDF2
- Pandas
- Matplotlib
- Regular Expressions (Regex)
- Collections — Counter

## 💼 Supported Job Roles

The application currently supports these job roles:

### 1. Data Scientist
- Python
- Machine Learning
- Data Science
- SQL
- NLP

### 2. Web Developer
- HTML
- CSS
- JavaScript
- Python

### 3. AI Engineer
- Python
- Deep Learning
- TensorFlow
- Machine Learning
- NLP

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or later
- pip package manager

### Step 1: Clone the Repository

```bash
git clone https://github.com/prathu-24/AI-Resume-Analyzer.git
```

### Step 2: Navigate to the Project Folder

```bash
cd AI-Resume-Analyzer
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
streamlit run app.py
```

The application should open in your default browser at:

`http://localhost:8501`

## 🔍 How It Works

1. Select a job role from the dropdown menu.
2. Upload a resume in PDF format.
3. Extract text from the uploaded resume.
4. Detect email addresses and phone numbers.
5. Identify skills using keyword matching.
6. Compare detected skills against the selected role's required skills.
7. Calculate and display the skill-matching percentage.
8. Show missing skills and suggestions for improvement.
9. Display a chart of the detected skills.

## 📊 ATS Compatibility Score

The application calculates a basic skill-matching score using the following formula:

**ATS Compatibility Score = (Matched Required Skills / Total Required Skills) × 100**

This score represents keyword-based skill compatibility. It is not an official score from an Applicant Tracking System and does not guarantee selection for a job.

## 📁 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
└── README.md
```

## 🔮 Future Enhancements

- Add NLP-based skill extraction.
- Support DOCX resume uploads.
- Match resumes against uploaded job descriptions.
- Use semantic similarity to identify related skills.
- Generate downloadable resume analysis reports.
- Add resume improvement recommendations based on job descriptions.

## ⚠️ Limitations

- Skill detection relies on predefined keywords.
- Skills expressed using different wording may not be detected.
- PDF files containing scanned images may require OCR.
- Contact extraction may not work correctly for every resume format.
- The compatibility score evaluates selected skills rather than overall candidate suitability.

## 👨‍💻 Project Overview

**AI Resume Analyzer** demonstrates the use of Python, document processing, text extraction, keyword-based analysis, and interactive data visualization to assist with resume evaluation.

