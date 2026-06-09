# Sentiment Analyzer

A full-stack machine learning web app that predicts the sentiment of any text as **positive**, **negative**, or **neutral**. Type or paste any text and get an instant prediction with a confidence score, powered by a Logistic Regression model trained on 14,000+ real airline tweets.

🔗 **Live Demo:** https://sentiment-app-taupe.vercel.app/

---

## Screenshot

> _Add a screenshot or GIF of the UI here_

---

## Tech Stack

| Layer | Technology |
|---|---|
| Machine Learning | scikit-learn (TF-IDF + Logistic Regression) |
| Backend | FastAPI + Uvicorn |
| Frontend | React, Next.js, Tailwind CSS |
| Backend Hosting | Render |
| Frontend Hosting | Vercel |
| Version Control | GitHub |

---

## Model Performance

Trained on the [Twitter US Airline Sentiment](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment) dataset (14,000+ tweets).

| Metric | Score |
|---|---|
| Overall Accuracy | **80.7%** |
| Negative F1 | 0.88 |
| Neutral F1 | 0.60 |
| Positive F1 | 0.70 |

The model performs strongest on negative sentiment, which reflects the natural class imbalance in the dataset — negative tweets make up the majority of the data. Neutral is the hardest class to predict, which is common in sentiment analysis since neutral text lacks strong signal words.

---

## Dataset

**Twitter US Airline Sentiment** — a Kaggle dataset containing 14,000+ tweets directed at major US airlines, labeled as positive, negative, or neutral.

I chose this dataset because it is real, messy, domain-specific social media text. Unlike clean movie review datasets, airline tweets contain slang, sarcasm, abbreviations, and heavy class imbalance — which made preprocessing and evaluation more challenging and more realistic.

---

## How to Run Locally

### Prerequisites
- Python 3.11+
- Node.js 18+
- Kaggle account (to download the dataset)

### 1. Clone the repo
```bash
git clone https://github.com/madiiyer16/SentimentApp.git
cd SentimentApp
```

### 2. Set up the backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
pip install -r requirements.txt
```

### 3. Train the model
Download `Tweets.csv` from [Kaggle](https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment) and place it in the `backend/` folder, then:
```bash
python train.py
```
This generates `model.pkl` and `vectorizer.pkl`.

### 4. Start the backend
```bash
uvicorn main:app --reload
```
Backend runs at `http://127.0.0.1:8000`

### 5. Set up the frontend
```bash
cd ../frontend
npm install
```

Create a `.env.local` file in the `frontend/` folder:
```
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

### 6. Start the frontend
```bash
npm run dev
```
Frontend runs at `http://localhost:3000`

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Check if the API is running |
| POST | `/predict` | Predict sentiment of input text |

**POST /predict — Request:**
```json
{ "text": "The flight was cancelled with no warning." }
```

**POST /predict — Response:**
```json
{
  "sentiment": "negative",
  "confidence": 0.9421,
  "input_text": "The flight was cancelled with no warning."
}
```

---

## What I Would Improve With More Time

- **Add a transformer model** — swap in DistilBERT from HuggingFace and let users compare results between the simple model and the transformer
- **Handle class imbalance** — apply SMOTE or class weighting to improve neutral and positive F1 scores
- **Batch analysis** — let users paste multiple sentences and get per-sentence predictions
- **Confidence bar chart** — show probability scores for all three classes instead of just the predicted one
- **Better preprocessing** — handle sarcasm, slang, and negation more carefully (e.g. "not great" should not be positive)

---

## Author

Madi Iyer — [GitHub](https://github.com/madiiyer16)
