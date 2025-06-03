import re
import pickle
import argparse
import os

# Diacritics and Punctuations
OTHER = ' '
DIACRITICS = [OTHER, "َ", "ً", "ُ", "ٌ", "ِ", "ٍ", "ْ", "ّ", "َّ", "ًّ", "ُّ", "ٌّ", "ِّ", "ٍّ"]
PUNCTUATIONS = [".", "،", ":", "؛", "؟"]

# Load Main Diacritics
with open("./utils/diacritics.pickle", "rb") as file:
    MAIN_DIACRITICS = list(pickle.load(file))

# Load Arabic Letters
with open("./utils/arabic_letters.pickle", "rb") as file:
    basic_arabic_letters = list(pickle.load(file))

VALID_ARABIC_CHARS = basic_arabic_letters + MAIN_DIACRITICS + PUNCTUATIONS + [' ']
ONLY_ARABIC_CHARS = basic_arabic_letters + MAIN_DIACRITICS + [' ', '.'] 

# Replace single Arabic letters surrounded by spaces (like " ب ") with just the letter (like "ب")
SINGLE_LETTER_PATTERN = re.compile(r'\s[' + ''.join(basic_arabic_letters) + r']\s')

# Regex for whitespace normalization
WHITESPACES_PATTERN = re.compile(r"\s+")

def preprocess(text, valid_chars=ONLY_ARABIC_CHARS):
    """Preprocess text by removing invalid chars and normalizing whitespace."""
    filtered_text = ''.join(ch if ch in valid_chars else ' ' for ch in text)
    collapsed_text = WHITESPACES_PATTERN.sub(' ', filtered_text)
    collapsed_text = SINGLE_LETTER_PATTERN.sub(' ', collapsed_text)
    return collapsed_text.strip()

def preprocess_file(input_path, output_dir="preprocessed", keep_punctuation=False):

    os.makedirs(output_dir, exist_ok=True)
    
    valid_chars = VALID_ARABIC_CHARS if keep_punctuation else ONLY_ARABIC_CHARS
    
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    processed_text = preprocess(text, valid_chars)
    
    filename = os.path.basename(input_path)
    output_path = os.path.join(output_dir, filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(processed_text)
    
    print(f"✅ Preprocessed file saved to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Preprocess Arabic text files.")
    parser.add_argument("input_file", help="Path to the input .txt file")
    parser.add_argument("--keep-punctuation", action="store_true", help="Keep punctuation marks (.,:؛؟)")
    args = parser.parse_args()
    
    preprocess_file(args.input_file, keep_punctuation=args.keep_punctuation)
