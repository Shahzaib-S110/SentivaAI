import streamlit as st
import joblib
import re
import emoji

# ===============================
# Load Model + Vectorizer
# ===============================
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# ===============================
# Preprocessing Function
# ===============================
def preprocess_roman_urdu(text):
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = emoji.demojize(text, delimiters=(" ", " "))
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'<.*?>', '', text)

    roman_urdu_map = {
        r'\bacha\b': 'acha',
        r'\bbht\b': 'bohot',
        r'\bbhut\b': 'bohot',
        r'\bbhot\b': 'bohot',
        r'\bbohat\b': 'bohot',
        r'\bnhi\b': 'nahi',
        r'\bkrna\b': 'karna',
        r'\bkr\b': 'kar',
        r'\bphr\b': 'phir',
        r'\bmje\b': 'mujhe',
        r'\bor\b': 'aur',
        r'\bgood\b': 'good',
        r'\bbad\b': 'bad',
    }

    for pattern, replacement in roman_urdu_map.items():
        text = re.sub(pattern, replacement, text)

    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    return text

# ===============================
# Prediction Function
# ===============================
def predict_sentiment(text):
    clean_text = preprocess_roman_urdu(text)
    vector = vectorizer.transform([clean_text])
    prediction = model.predict(vector)[0]

    return prediction

# ===============================
# Streamlit UI
# ===============================
st.set_page_config(page_title="Roman Urdu Sentiment Analyzer", page_icon="🧠")

st.title("🛍️ Roman Urdu Sentiment Analyzer")
st.write("Enter a product review in Roman Urdu and get sentiment prediction.")

# Input box
user_input = st.text_area("✍️ Enter your review here:")

# Button
if st.button("Predict Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text first!")
    else:
        result = predict_sentiment(user_input)

        # Map labels (adjust if needed)
        label_map = {
            0: "❌ Negative",
            1: "😐 Neutral",
            2: "✅ Positive"
        }

        st.success(f"Prediction: {label_map.get(result, result)}")