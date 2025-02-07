import re
import pickle

# Diacritics and Punctuations
OTHER = ' '
DIACRITICS = [OTHER, "َ", "ً", "ُ", "ٌ", "ِ", "ٍ", "ْ", "ّ", "َّ", "ًّ", "ُّ", "ٌّ", "ِّ", "ٍّ"]
PUNCTUATIONS = [".", "،", ":", "؛", "؟"]

# Main Diacritics
with open("./utils/diacritics.pickle", "rb") as file:
    MAIN_DIACRITICS = list(pickle.load(file))

# Arabic Letters
with open("./utils/arabic_letters.pickle", "rb") as file:
    basic_arabic_letters = list(pickle.load(file))

VALID_ARABIC_CHARS = basic_arabic_letters + MAIN_DIACRITICS + PUNCTUATIONS + [' ']

# one or more whitespace characters
WHITESPACES_PATTERN = re.compile(r"\s+")

def preprocess(text, valid_chars=VALID_ARABIC_CHARS):
    # remove any character not in the allowed list
    filtered_text = ''.join(ch for ch in text if ch in valid_chars)
    
    # collapse multiple whitespace characters into a single space
    collapsed_text = WHITESPACES_PATTERN.sub(' ', filtered_text)
    
    # remove leading and trailing whitespace
    return collapsed_text.strip()