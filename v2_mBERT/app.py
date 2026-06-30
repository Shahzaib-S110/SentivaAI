import streamlit as st
from utils import (
    normalize_text,
    format_confidence,
    load_history,
    save_history,
    add_to_history
)

from predictor import predict_sentiment

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="SentivaAI - Roman Urdu Sentiment Analyzer",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 SentivaAI - Roman Urdu Sentiment Analyzer")
st.markdown("Analyze **Roman Urdu reviews** with AI-powered sentiment detection")

# -----------------------------
# Load history
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = load_history()

# -----------------------------
# Input Box
# -----------------------------
user_input = st.text_area("Enter Roman Urdu text:")

if st.button("Analyze Sentiment"):
    if user_input.strip():

        # Normalize
        cleaned_text = normalize_text(user_input)

        # Predict
        label, confidence = predict_sentiment(cleaned_text)

        # Format
        conf_percent = format_confidence(confidence)

        # Show result
        st.subheader("Result")
        st.write(f"**Sentiment:** {label}")
        st.write(f"**Confidence:** {conf_percent}")

        # Save history
        st.session_state.history = add_to_history(
            st.session_state.history,
            user_input,
            label,
            conf_percent
        )
        save_history(st.session_state.history)

    else:
        st.warning("Please enter some text.")

# -----------------------------
# History Section
# -----------------------------
st.divider()
st.subheader("📜 Session History")

if st.session_state.history:
    for item in reversed(st.session_state.history[-10:]):
        st.write(f"📝 {item['text']}")
        st.write(f"➡️ {item['label']} ({item['confidence']})")
        st.caption(item["time"])
        st.divider()
else:
    st.info("No history yet.")