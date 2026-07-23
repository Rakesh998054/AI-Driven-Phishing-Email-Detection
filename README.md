# 🛡️ AI-Driven Phishing Email Detection Using NLP and Machine Learning
<p align="center">

<a href="https://ai-driven-phishing-email-detection-khqkaep8lwtbr88hhhxvmd.streamlit.app">
  <img src="https://img.shields.io/badge/🚀%20Live%20Demo-Try%20Now-success?style=for-the-badge" alt="Live Demo">
</a>

<a href="https://github.com/ashutoshsharma-08/AI-Driven-Phishing-Email-Detection">
  <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub Repository">
</a>

</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg">
  <img src="https://img.shields.io/badge/Framework-Streamlit-red.svg">
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange.svg">
  <img src="https://img.shields.io/badge/NLP-TF--IDF-green.svg">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg">
</p>

## 📌 Overview

AI-Driven Phishing Email Detection Using NLP is a Machine Learning-based web application that automatically classifies emails as **Phishing** or **Legitimate**.

The project uses **Natural Language Processing (NLP)** techniques to clean and preprocess email text, converts textual information into numerical features using **TF-IDF Vectorization**, and applies multiple Machine Learning algorithms to identify phishing emails accurately.

The trained model is deployed through a **Streamlit** web application, allowing users to analyze email content in real time with prediction confidence and useful statistics.

---

## ✨ Features

- Detects phishing and legitimate emails instantly
- Text preprocessing using NLP techniques
- TF-IDF feature extraction
- Comparison of multiple Machine Learning models
- Interactive Streamlit web application
- Displays prediction confidence score
- Shows email statistics
- User-friendly interface
- High prediction accuracy

---

## 🎯 Objectives

- Detect phishing emails automatically.
- Reduce the risk of cyber attacks.
- Compare different Machine Learning algorithms.
- Develop a real-time phishing email detection system.
- Provide an easy-to-use web interface for users.

---

## 🛠 Technologies Used

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Machine Learning | Scikit-Learn |
| NLP | NLTK |
| Feature Extraction | TF-IDF Vectorizer |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Web Application | Streamlit |
| Version Control | Git & GitHub |

---

## 🧠 Machine Learning Models

The following algorithms were trained and evaluated:

- Logistic Regression
- Multinomial Naive Bayes
- Random Forest Classifier
- Support Vector Machine (Linear SVM)
- Multi-Layer Perceptron (MLP)

Among all models, **Logistic Regression** achieved the best performance and was selected for deployment.

---

## 📊 Model Performance

| Metric | Score |
|---------|--------|
| Accuracy | 97.95% |
| Precision | 97.78% |
| Recall | 98.30% |
| F1-Score | 98.04% |

---

## 📂 Project Structure

```text
AI_Driven_Phishing_Email_Detection
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
│
├── dataset/
│   └── phishing_email.csv (Not included in GitHub)
│
├── models/
│   ├── best_phishing_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── notebook/
│   └── AI_Driven_Phishing_Email_Detection.ipynb
│
└── screenshots/
```

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/ashutoshsharma-08/AI-Driven-Phishing-Email-Detection.git
```

### Move into the project folder

```bash
cd AI-Driven-Phishing-Email-Detection
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run app.py
```

---

## 💻 Application Workflow

1. Enter email text.
2. Click **Analyze Email**.
3. Email is preprocessed using NLP.
4. TF-IDF converts text into numerical features.
5. Machine Learning model predicts the result.
6. Prediction, confidence score, and email statistics are displayed.

---

## 📈 Future Improvements

- Deep Learning (LSTM/BERT)
- URL feature extraction
- Attachment analysis
- Email header analysis
- Multi-language phishing detection
- Cloud deployment
- API integration

---

## 👨‍💻 Developer

**Ashutosh Sharma**

B.Tech Computer Science Engineering (AI & DS)

Government Hydro Engineering College, Bandla, Bilaspur (H.P.)

GitHub: https://github.com/ashutoshsharma-08

---

## ⭐ Support

If you found this project useful, consider giving this repository a ⭐ on GitHub.

---

# 📸 Application Screenshots

## 🏠 Home Page

The home page provides a clean and interactive interface where users can enter the email content for phishing analysis.

<p align="center">
  <img src="screenshots/home.png" alt="Home Page" width="900">
</p>

---

## 📧 Email Prediction

After clicking **Analyze Email**, the machine learning model predicts whether the email is **Phishing** or **Legitimate** along with the confidence score.

<p align="center">
  <img src="screenshots/prediction.png" alt="Prediction" width="900">
</p>

---

## ⚠️ Risk Analysis

The application displays the risk level based on the prediction confidence, helping users understand how dangerous the email may be.

<p align="center">
  <img src="screenshots/risk.png" alt="Risk Analysis" width="900">
</p>

---

## 📊 Email Statistics

The application also provides useful statistics such as:

- Total Characters
- Total Words
- Number of URLs
- Email Addresses
- Suspicious Keywords
- Prediction Confidence

<p align="center">
  <img src="screenshots/statistics.png" alt="Email Statistics" width="900">
</p>

---