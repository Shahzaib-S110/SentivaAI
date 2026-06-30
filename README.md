# 🛍️ SentivaAI
### AI-Powered Roman Urdu Product Review Sentiment Analyzer

🔗 **Live Demo:** https://sentiva-ai.streamlit.app/
**Live Demo:** https://huggingface.co/Shahzaib110/finetune_mBERT

---

# 📖 About

**SentivaAI** is an AI-powered sentiment analysis platform designed specifically for **Roman Urdu product reviews**. The project analyzes customer feedback collected from **Daraz.pk** and classifies reviews into **Positive**, **Neutral**, and **Negative** sentiments.

The project evolved from a traditional Machine Learning approach (TF-IDF + Logistic Regression) to a state-of-the-art **Multilingual BERT (mBERT)** deep learning model, significantly improving performance on code-mixed Roman Urdu and English text.

---

# 📊 Dataset

- 🛒 **16,990** real product reviews scraped from **Daraz.pk**
- 🇵🇰 Roman Urdu + English (Code-Mixed)
- 😊 Positive
- 😐 Neutral
- 😞 Negative
- Class imbalance handled using resampling techniques

---

# 🚀 Project Evolution

## 🔹 Version 1 — TF-IDF + Logistic Regression

Classical Machine Learning baseline model using TF-IDF feature extraction and Logistic Regression classifier.

### Performance

| Metric | Score |
|---------|------:|
| Overall Accuracy | **92.3%** |
| Precision | **92%** |
| Recall | **92%** |
| F1-Score | **92%** |

### Class-wise Accuracy

| Sentiment | Accuracy |
|------------|---------:|
| 😞 Negative | **93.6%** |
| 😐 Neutral | **92.6%** |
| 😊 Positive | **90.7%** |

**Model Stack**

- TF-IDF Vectorizer
- Logistic Regression
- Scikit-learn
- Streamlit

📓 **Notebook:** `SentivaAI_V1.ipynb`

---

# ⭐ Version 2 — Multilingual BERT (Current)

Fine-tuned **bert-base-multilingual-cased** model optimized for Roman Urdu sentiment classification.

The model understands:

- Roman Urdu
- Code-Mixed English
- Slang
- Misspellings
- Informal language
- Emojis

### Performance

| Metric | Score |
|---------|------:|
| Overall Accuracy | **96%** |
| Precision | **96%** |
| Recall | **96%** |
| F1-Score | **96%** |
| ROC-AUC | **0.99** |

### Class-wise Accuracy

| Sentiment | Accuracy |
|------------|---------:|
| 😞 Negative | **97%** |
| 😐 Neutral | **95%** |
| 😊 Positive | **95%** |

### Model

```
bert-base-multilingual-cased
```

Fine-tuned using:

- Hugging Face Transformers
- PyTorch

📓 **Notebook:** `SentivaAI_V2_mBERT.ipynb`

---

# ✨ Features

- 🤖 AI-powered Roman Urdu sentiment analysis
- 📈 Confidence score with progress bar
- 💡 Seller action recommendations
- 📝 Session history tracking
- 🔤 Roman Urdu slang normalization
- 🌍 Code-mixed language support
- 📊 Interactive Streamlit dashboard
- ⚡ Fast inference using mBERT
- 📂 Batch review prediction
- 📋 Prediction confidence breakdown

---

# 🛠️ Tech Stack

| Component | Version 1 | Version 2 |
|------------|-----------|-----------|
| Language | Python | Python |
| ML Framework | Scikit-learn | Hugging Face Transformers |
| Model | Logistic Regression | mBERT |
| Feature Extraction | TF-IDF | Transformer Embeddings |
| Deep Learning | — | PyTorch |
| Frontend | Streamlit | Streamlit |
| Data Processing | Pandas | Pandas |
| Visualization | Matplotlib | Streamlit |

---

# 📁 Project Structure

```
SentivaAI/
│
├── app.py
├── predictor.py
├── preprocessing.py
├── config.py
├── utils.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── V1_LogisticRegression/
│   └── V2_mBERT/
│
├── assets/
│   ├── logo.png
│   └── banner.png
│
├── pages/
│   ├── Dashboard.py
│   ├── History.py
│   └── About.py
│
├── notebooks/
│   ├── SentivaAI_V1.ipynb
│   └── SentivaAI_V2_mBERT.ipynb
│
└── data/
    └── history.csv
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/SentivaAI.git
```

Move into the project directory

```bash
cd SentivaAI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 🎯 Supported Sentiments

| Label | Meaning |
|-------|---------|
| 😊 Positive | Customer is satisfied |
| 😐 Neutral | Mixed or objective opinion |
| 😞 Negative | Customer is dissatisfied |

---

# 📈 Model Comparison

| Feature | V1 | V2 |
|----------|----|----|
| TF-IDF | ✅ | ❌ |
| Logistic Regression | ✅ | ❌ |
| mBERT | ❌ | ✅ |
| Roman Urdu Support | Good | Excellent |
| Code-Mixed Language | Moderate | Excellent |
| Slang Understanding | Limited | Excellent |
| Emoji Understanding | ❌ | ✅ |
| Deep Context Understanding | ❌ | ✅ |
| Overall Accuracy | **92.3%** | **96%** |

---

# 🔮 Future Improvements

- 🌐 Multilingual sentiment analysis
- 😊 Emotion detection
- 🛡️ Fake review detection
- 📊 Explainable AI (XAI)
- 📱 Mobile application
- ☁️ REST API deployment
- 🐳 Docker support
- ⚡ Real-time analytics dashboard
- 🛍️ Seller recommendation engine
- 📈 Advanced business insights

---

# 👨‍💻 Author

**Shahzaib Saleem**

Computer Science Student

AI Engineer | Machine Learning Enthusiast | Full-Stack Developer

- GitHub: https://github.com/yourusername
- LinkedIn: https://linkedin.com/in/yourprofile
- Hugging Face: https://huggingface.co/codeZ1234

---

# 📄 License

This project is released under the **MIT License**.

You are free to use, modify, and distribute this project for educational and research purposes.

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

Your support helps improve future AI and NLP projects.
