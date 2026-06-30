# SentivaAI v2 (mBERT)

SentivaAI v2 is an advanced multilingual sentiment analysis system powered by Multilingual BERT (mBERT). It is specifically optimized for Roman Urdu sentiment classification and provides confidence scores with an interactive Streamlit interface.

## Features

- Fine-tuned mBERT Model
- Roman Urdu preprocessing
- Confidence prediction
- Batch prediction
- Session history
- Interactive dashboard
- Streamlit UI

## Technologies

- Python
- PyTorch
- HuggingFace Transformers
- Streamlit
- Pandas
- NumPy

## Folder Structure

```
SentivaAI/
│
├── app.py
├── predictor.py
├── preprocessing.py
├── config.py
├── utils.py
├── assets/
├── pages/
├── models/
├── data/
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

Run

```bash
streamlit run app.py
```

## Model

Model: Multilingual BERT (mBERT)

Classes

- Positive
- Neutral
- Negative

## Future Improvements

- Explainable AI
- Emotion Detection
- Fake Review Detection
- REST API
- Docker Deployment

## Author

Shahzaib Saleem