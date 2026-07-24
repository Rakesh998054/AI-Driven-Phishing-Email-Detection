import streamlit as st

st.set_page_config(
    page_title="AI-Driven Phishing Email Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================
# PAGE CONFIGURATION
# ======================================

st.set_page_config(
    page_title="AI-Driven Phishing Email Detection",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================
# CUSTOM CSS
# ======================================

st.markdown("""
<style>

.stApp{
    background-color:#0E1117;
}

/* Hero Title */

.hero-title{
    font-size:80px;
    font-weight:900;
    color:#64B5F6;
    text-align:center;
    line-height:1.1;
    margin-top:10px;
    margin-bottom:15px;
}

/* Hero Subtitle */

.hero-subtitle{
    font-size:30px;
    color:#EAEAEA;
    text-align:center;
    font-weight:500;
    line-height:1.6;
    margin-bottom:35px;
}

/* Footer */

.footer{
    text-align:center;
    color:gray;
    font-size:16px;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)
# ======================================
# SIDEBAR
# ======================================

st.sidebar.image(
    "https://img.icons8.com/color/96/artificial-intelligence.png",
    width=90
)

st.sidebar.title("AI Phishing Detector")

st.sidebar.markdown("---")

st.sidebar.markdown("### 👨‍💻 Developed By")

st.sidebar.success("""
**Rakesh**

B.Tech Student

NMAM institute of technology , Nitte (ISE)
""")

st.sidebar.markdown("---")

st.sidebar.markdown("### 📚 Project")

st.sidebar.info("""
AI-Driven Phishing Email Detection

✔ NLP

✔ Machine Learning

✔ TF-IDF

✔ Logistic Regression
""")

st.sidebar.markdown("---")

st.sidebar.markdown("### 📧 Features")

st.sidebar.write("✅ Email Classification")

st.sidebar.write("✅ Confidence Score")

st.sidebar.write("✅ Risk Level")

st.sidebar.write("✅ Email Statistics")

st.sidebar.write("✅ Security Recommendations")

# ======================================
# MAIN PAGE
# ======================================

st.markdown("""
<div style="text-align:center; padding:15px 0px;">

<h1 style="
font-size:48px;
font-weight:800;
color:#64B5F6;
margin-bottom:12px;
">

📧 AI-Driven Phishing Email Detection

</h1>

<p style="
font-size:20px;
color:#E5E7EB;
line-height:1.5;
margin-bottom:10px;
">

Detect phishing emails using
<b>Artificial Intelligence</b>,
<b>Natural Language Processing (NLP)</b>
and
<b>Machine Learning</b>.

</p>

<p style="
font-size:17px;
color:#BDBDBD;
">

Paste an email below and click **Analyze Email** to detect whether it is phishing or legitimate.

</p>

</div>
""", unsafe_allow_html=True)

st.divider()

st.header("📩 Email Analysis")

email_text = st.text_area(
    "Paste Email Content",
    height=250,
    placeholder="Paste your email here..."
)



predict_button = st.button(
    "🔍 Analyze Email",
    use_container_width=True
)


import pandas as pd
import numpy as np
import joblib
import re
import string
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")


model = joblib.load("best_phishing_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def clean_text(text):

    text = text.lower()

    text = re.sub(r"http\S+|www\S+", " ", text)

    text = re.sub(r"\S+@\S+", " ", text)

    text = re.sub(r"<.*?>", " ", text)

    text = re.sub(r"\d+", " ", text)

    text = text.translate(str.maketrans("", "", string.punctuation))

    text = re.sub(r"\s+", " ", text).strip()

    words = word_tokenize(text)

    words = [w for w in words if w not in stop_words]

    words = [lemmatizer.lemmatize(w) for w in words]

    return " ".join(words)

def predict_email(email):

    cleaned = clean_text(email)

    vector = tfidf.transform([cleaned])

    prediction = model.predict(vector)[0]

    probability = model.predict_proba(vector)[0]

    return prediction, probability

# ======================================
# ANALYZE EMAIL
# ======================================

if predict_button:

    if email_text.strip() == "":
        st.warning("⚠️ Please enter an email.")

    else:

        # Predict
        prediction, probability = predict_email(email_text)

        confidence = max(probability) * 100

        st.divider()

        # ============================
        # Prediction Result
        # ============================

        st.header("🎯 Prediction Result")

        if prediction == 1:

            st.error("🚨 PHISHING EMAIL DETECTED")

            st.metric(
                label="Confidence",
                value=f"{confidence:.2f}%"
            )

        else:

            st.success("✅ LEGITIMATE EMAIL")

            st.metric(
                label="Confidence",
                value=f"{confidence:.2f}%"
            )
        # ============================
        # Email Statistics
        # ============================

        st.divider()

        st.header("📊 Email Statistics")

        words = email_text.split()

        url_count = len(re.findall(r"http\S+|www\S+", email_text))

        email_count = len(re.findall(r"\S+@\S+", email_text))

        suspicious_words = [
            "urgent","verify","bank","password",
            "login","account","click","free",
            "winner","offer","gift","limited",
            "security","confirm","update"
        ]

        suspicious_count = sum(
            word.lower() in suspicious_words
            for word in words
        )

        col1, col2, col3 = st.columns(3)

        col1.metric("Characters", len(email_text))
        col2.metric("Words", len(words))
        col3.metric("URLs", url_count)

        col4, col5 = st.columns(2)

        col4.metric("Email Addresses", email_count)
        col5.metric("Suspicious Keywords", suspicious_count)
        
        # ============================
        # Risk Level
        # ============================

        st.divider()

        st.header("⚠️ Risk Level")

        if prediction == 1:

            if confidence >= 95:

                st.error("🔴 HIGH RISK")

            elif confidence >= 80:

                st.warning("🟠 MEDIUM RISK")

            else:

                st.info("🟡 LOW RISK")

        else:

            st.success("🟢 SAFE EMAIL")
        # ============================
        # Recommendations
        # ============================

        st.divider()

        st.header("🛡️ Security Recommendations")

        if prediction == 1:

            st.error("""
• Do not click suspicious links.

• Do not download unknown attachments.

• Verify the sender before replying.

• Report the email as phishing.

• Delete the email immediately.
""")

        else:

            st.success("""
• No phishing indicators detected.

• Continue following good email security practices.

• Verify unknown senders.

• Keep your antivirus updated.
""")
            
# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

footer = """
<div style="text-align:center; padding:20px;">

<h2 style="color:#00C4FF;">
👨‍💻 Developed by Rakesh
</h2>

<p style="font-size:18px;">
<b>B.Tech Student</b><br>
NMAM institute of technology , Nitte (ISE)
</p>

<p style="color:gray;">
AI-Driven Phishing Email Detection using NLP & Machine Learning
</p>

<p style="color:gray;">
© 2026 Rakesh | All Rights Reserved
</p>

</div>
"""

st.markdown(footer, unsafe_allow_html=True)