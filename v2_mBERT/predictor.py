"""
Prediction module for Sentiva AI (mBERT-based)
"""

import torch
import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification

from preprocessing import preprocess
from config import (
    MODEL_NAME,
    DEVICE,
    MAX_LENGTH,
    LABELS,
    LABEL_ICONS,
)

# ----------------------------------------------------
# Load Model (cached)
# ----------------------------------------------------

@st.cache_resource
def load_model():
    print("Loading mBERT model from Hugging Face...")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

    model.to(DEVICE)
    model.eval()

    print("Model loaded successfully.")

    return tokenizer, model


tokenizer, model = load_model()

# ----------------------------------------------------
# Single Prediction
# ----------------------------------------------------

def predict_sentiment(review: str):
    clean_review = preprocess(review)

    inputs = tokenizer(
        clean_review,
        return_tensors="pt",
        truncation=True,
        padding="max_length",
        max_length=MAX_LENGTH,
    )

    inputs = {k: v.to(DEVICE) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)

        probabilities = torch.softmax(outputs.logits, dim=1)[0]
        prediction_id = torch.argmax(outputs.logits, dim=1).item()

    label = LABELS[prediction_id]
    confidence = float(probabilities[prediction_id])

    return label, confidence


# ----------------------------------------------------
# Detailed Prediction
# ----------------------------------------------------

def predict_sentiment_full(review: str):
    clean_review = preprocess(review)

    inputs = tokenizer(
        clean_review,
        return_tensors="pt",
        truncation=True,
        padding="max_length",
        max_length=MAX_LENGTH,
    )

    inputs = {k: v.to(DEVICE) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)

        probabilities = torch.softmax(outputs.logits, dim=1)[0]
        prediction_id = torch.argmax(outputs.logits, dim=1).item()

    return {
        "review": review,
        "clean_review": clean_review,
        "prediction_id": prediction_id,
        "label": LABELS[prediction_id],
        "icon": LABEL_ICONS[prediction_id],
        "confidence": float(probabilities[prediction_id]),
        "negative": float(probabilities[0]),
        "neutral": float(probabilities[1]),
        "positive": float(probabilities[2]),
    }


# ----------------------------------------------------
# Batch Prediction
# ----------------------------------------------------

def predict_batch(reviews):
    return [predict_sentiment_full(review) for review in reviews]