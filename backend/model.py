import joblib
from preprocess import clean_text

# Load the saved model and vectorizer from disk
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Map numeric predictions back to readable labels
label_map = {0: 'negative', 1: 'neutral', 2: 'positive'}

def predict_sentiment(text: str):
    # Clean the input the same way we cleaned training data
    cleaned = clean_text(text)
    
    # Transform text into TF-IDF vector
    vectorized = vectorizer.transform([cleaned])
    
    # Get the predicted class (0, 1, or 2)
    prediction = model.predict(vectorized)[0]
    
    # Get confidence score (probability of the predicted class)
    confidence = model.predict_proba(vectorized)[0][prediction]
    
    return {
        "sentiment": label_map[prediction],
        "confidence": round(float(confidence), 4)
    }