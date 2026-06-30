import streamlit as st
from utils import normalize_text, format_confidence
from predictor import predict_sentiment
import pandas as pd
import os

st.title("📊 SentivaAI Dashboard")

# -----------------------------
# Banner (optional)
# -----------------------------
st.image("assets/banner.jpg", use_container_width=True)

# -----------------------------
# Input
# -----------------------------
text = st.text_area("Enter Roman Urdu text")

if st.button("Analyze"):
    if text.strip():

        cleaned = normalize_text(text)
        label, confidence = predict_sentiment(cleaned)
        conf_percent = format_confidence(confidence)

        st.success(f"Sentiment: {label}")
        st.info(f"Confidence: {conf_percent}")

    else:
        st.warning("Please enter text.")

# -----------------------------
# Quick Stats (if CSV exists)
# -----------------------------
file_path = "data/history.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)

    st.subheader("📈 Quick Stats")

    st.write("Total Records:", len(df))
    st.write("Positive:", len(df[df["label"] == "Positive"]))
    st.write("Negative:", len(df[df["label"] == "Negative"]))