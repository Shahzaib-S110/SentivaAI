import re
import json
from datetime import datetime

# -----------------------------
# Roman Urdu normalization map
# -----------------------------
SLANG_MAP = {
    "gr8": "great",
    "btw": "by the way",
    "u": "you",
    "ur": "your",
    "kya": "what",
    "acha": "good",
    "nahi": "no",
    "hn": "yes",
    "h": "is",
    "hy": "is",
    "bht": "very",
    "bohat": "very",
    "plz": "please"
}

def normalize_text(text: str) -> str:
    """Normalize Roman Urdu / slang text."""
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)  # remove URLs
    text = re.sub(r"[^\w\s]", "", text)         # remove punctuation

    words = text.split()
    cleaned_words = [SLANG_MAP.get(w, w) for w in words]

    return " ".join(cleaned_words)


# -----------------------------
# Confidence formatting
# -----------------------------
def format_confidence(score: float) -> str:
    return f"{round(score * 100, 2)}%"


# -----------------------------
# Session history tracking
# -----------------------------
def save_history(history, file="history.json"):
    with open(file, "w") as f:
        json.dump(history, f, indent=4)


def load_history(file="history.json"):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def add_to_history(history, text, label, confidence):
    history.append({
        "text": text,
        "label": label,
        "confidence": confidence,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    return history