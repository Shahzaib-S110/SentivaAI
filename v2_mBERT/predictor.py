"""
Prediction module for Sentiva AI (mBERT-based)
"""

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

from preprocessing import preprocess
from config import MODEL_DIR, DEVICE, MAX_LENGTH, LABELS, LABEL_ICONS

# ----------------------------------------------------
# Load Model (runs once when app starts)
# ----------------------------------------------------

print("Loading mBERT model...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)

model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)

model.to(DEVICE)
model.eval()

print("Model Loaded Successfully.")

# ----------------------------------------------------
# Single Prediction
# ----------------------------------------------------

def predict_sentiment(review: str):
    """
    Returns:
    label (str), confidence (float)
    """

    clean_review = preprocess(review)

    inputs = tokenizer(
        clean_review,
        return_tensors="pt",
        truncation=True,
        padding="max_length",
        max_length=MAX_LENGTH
    )

    # move to device
    inputs = {k: v.to(DEVICE) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)

        probabilities = torch.softmax(outputs.logits, dim=1)[0]

        prediction_id = torch.argmax(outputs.logits, dim=1).item()

    label = LABELS[prediction_id]
    confidence = float(probabilities[prediction_id])

    return label, confidence


# ----------------------------------------------------
# Detailed Prediction (optional advanced use)
# ----------------------------------------------------

def predict_sentiment_full(review: str):
    """
    Returns full breakdown (for dashboard analytics)
    """

    clean_review = preprocess(review)

    inputs = tokenizer(
        clean_review,
        return_tensors="pt",
        truncation=True,
        padding="max_length",
        max_length=MAX_LENGTH
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
    """
    Predict multiple reviews at once
    """
    return [predict_sentiment_full(r) for r in reviews]