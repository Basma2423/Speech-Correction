import re
import pickle

# Diacritics and punctuations
OTHER = ' '
DIACRITICS = [OTHER, "َ", "ً", "ُ", "ٌ", "ِ", "ٍ", "ْ", "ّ", "َّ", "ًّ", "ُّ", "ٌّ", "ِّ", "ٍّ"]
PUNCTUATIONS = [".", "،", ":", "؛", "؟"]

# Main diacritics
with open("./utils/diacritics.pickle", "rb") as file:
    MAIN_DIACRITICS = list(pickle.load(file))

# Arabic Letters
with open("./utils/arabic_letters.pickle", "rb") as file:
    basic_arabic_letters = list(pickle.load(file))

VALID_ARABIC_CHARS = basic_arabic_letters + MAIN_DIACRITICS + PUNCTUATIONS + [' ']

# One or more whitespace characters
WHITESPACES_PATTERN = re.compile(r"\s+")

def preprocess(text, valid_chars=VALID_ARABIC_CHARS):
    # Remove any character not in the allowed list
    filtered_text = ''.join(ch for ch in text if ch in valid_chars)
    
    # Collapse multiple whitespace characters into a single space
    collapsed_text = WHITESPACES_PATTERN.sub(' ', filtered_text)
    
    # Remove leading and trailing whitespace
    return collapsed_text.strip()