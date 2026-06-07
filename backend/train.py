import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from preprocess import clean_text

# ── 1. Load the dataset ──────────────────────────────────────────────────────
df = pd.read_csv('Tweets.csv')

# We only need the text and sentiment columns
df = df[['text', 'airline_sentiment']]

# Drop any rows where either column is missing
df = df.dropna()

# ── 2. Clean the text ────────────────────────────────────────────────────────
print("Cleaning text...")
df['clean'] = df['text'].apply(clean_text)

# ── 3. Map sentiment labels to numbers ───────────────────────────────────────
label_map = {'negative': 0, 'neutral': 1, 'positive': 2}
df['label'] = df['airline_sentiment'].map(label_map)

# ── 4. Split into train and test sets ────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    df['clean'],
    df['label'],
    test_size=0.2,       # 20% held back for testing
    random_state=42      # makes the split reproducible
)

# ── 5. Vectorize the text with TF-IDF ────────────────────────────────────────
print("Vectorizing...")
vectorizer = TfidfVectorizer(max_features=10000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec  = vectorizer.transform(X_test)    # transform only, NOT fit_transform

# ── 6. Train the model ───────────────────────────────────────────────────────
print("Training...")
model = LogisticRegression(max_iter=1000, C=1.0)
model.fit(X_train_vec, y_train)

# ── 7. Evaluate ──────────────────────────────────────────────────────────────
y_pred = model.predict(X_test_vec)
print("\nAccuracy:", model.score(X_test_vec, y_test))
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['negative', 'neutral', 'positive']))

# ── 8. Save model and vectorizer to disk ─────────────────────────────────────
joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
print("\nModel and vectorizer saved.")