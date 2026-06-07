import re

def clean_text(text):
    # 1. Lowercase everything
    text = text.lower()
    
    # 2. Remove URLs (http://..., https://..., www....)
    text = re.sub(r'http\S+|www\S+', '', text)
    
    # 3. Remove @mentions
    text = re.sub(r'@\w+', '', text)
    
    # 4. Remove hashtags (the # symbol, keep the word)
    text = re.sub(r'#', '', text)
    
    # 5. Remove punctuation and special characters (keep only letters and spaces)
    text = re.sub(r'[^a-z\s]', '', text)
    
    # 6. Collapse multiple spaces into one
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text