"""
Roman Urdu preprocessing
"""

import re
import emoji

# ----------------------------------------------------
# Roman Urdu Dictionary
# ----------------------------------------------------

ROMAN_DICT = {

    # Very Common

    "bht":"bohot",
    "bohat":"bohot",
    "bhot":"bohot",
    "bohut":"bohot",

    "acha":"acha",
    "achi":"acha",
    "achi":"acha",
    "achha":"acha",

    "thk":"theek",
    "thik":"theek",

    "kr":"kar",
    "krna":"karna",
    "krdia":"kar diya",
    "krdi":"kar di",

    "mje":"mujhe",
    "mjhe":"mujhe",

    "nhi":"nahi",
    "ni":"nahi",

    "phr":"phir",

    "plz":"please",

    "gud":"good",

    "awsm":"awesome",

    "zbrdast":"zabardast",

    "bekr":"bekar",

    "faltu":"bekar",

    "luv":"love",

    "frnd":"friend",

    "tym":"time",

    "msg":"message",

    "coz":"because"
}


# ----------------------------------------------------
# Preprocess Function
# ----------------------------------------------------

def preprocess(text):

    if not isinstance(text, str):
        return ""

    text = text.lower()

    # Convert emojis

    text = emoji.demojize(
        text,
        delimiters=(" ", " ")
    )

    # Remove URLs

    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"www\S+", "", text)

    # Remove HTML

    text = re.sub(r"<.*?>", "", text)

    # Remove @mentions

    text = re.sub(r"@\w+", "", text)

    # Remove hashtags

    text = re.sub(r"#", "", text)

    # Roman Urdu normalization

    words = text.split()

    normalized = []

    for word in words:

        normalized.append(
            ROMAN_DICT.get(word, word)
        )

    text = " ".join(normalized)

    # Remove punctuation

    text = re.sub(
        r"[^a-zA-Z0-9 ]",
        " ",
        text
    )

    # Remove extra spaces

    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    return text