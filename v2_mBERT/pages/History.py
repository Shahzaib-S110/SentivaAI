import streamlit as st
import pandas as pd
import os

st.title("📜 Sentiment History")

file_path = "data/history.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)

    st.dataframe(df, use_container_width=True)

    # -----------------------------
    # Filters
    # -----------------------------
    sentiment_filter = st.selectbox(
        "Filter by Sentiment",
        ["All", "Positive", "Negative"]
    )

    if sentiment_filter != "All":
        df = df[df["label"] == sentiment_filter]

    st.subheader("Filtered Results")
    st.dataframe(df, use_container_width=True)

else:
    st.warning("No history found. Run analysis first.")