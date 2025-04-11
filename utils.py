import re

def preprocess_text(text):
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    stopwords = set(["i", "am", "the", "a", "of", "and", "to", "in", "my", "on", "it", "for", "with"])
    words = text.split()
    filtered = [w for w in words if w not in stopwords]
    return ' '.join(filtered)
