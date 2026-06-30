"""
Configuration file for Sentiva AI
"""

import torch
from pathlib import Path

# ---------------------------------------------------
# Project Paths
# ---------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

MODEL_NAME = "Shahzaib110/finetune_mBERT"
# ---------------------------------------------------
# Device
# ---------------------------------------------------

DEVICE = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

# ---------------------------------------------------
# Model
# ---------------------------------------------------

MODEL_NAME = "Sentiva AI mBERT"

MAX_LENGTH = 256

# ---------------------------------------------------
# Labels
# ---------------------------------------------------

LABELS = {
    0: "Negative",
    1: "Neutral",
    2: "Positive"
}

LABEL_ICONS = {
    0: "🔴",
    1: "🟡",
    2: "🟢"
}

LABEL_COLORS = {
    0: "#ff4b4b",
    1: "#ffcc00",
    2: "#00c853"
}

# ---------------------------------------------------
# Seller Suggestions
# ---------------------------------------------------

SELLER_ACTIONS = {

    "Negative": [
        "Contact the customer immediately.",
        "Offer refund or replacement.",
        "Investigate product quality.",
        "Improve packaging.",
        "Respond professionally."
    ],

    "Neutral": [
        "Request detailed feedback.",
        "Clarify product description.",
        "Offer customer assistance.",
        "Improve delivery experience."
    ],

    "Positive": [
        "Thank the customer.",
        "Encourage another purchase.",
        "Ask for a product review.",
        "Recommend related products."
    ]
}