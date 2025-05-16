import random
from src.helping_dictionaries import keyboard_neighbors, phonetic_mapping, diacritic_mapping, DIACRITICS

KEYBOARD_ERROR_PROBABILITY = 0.02
ORDERING_ERROR_PROBABILITY = 0.02

PHONETIC_ERROR_PROBABILITY = 0.06
DIACRITIC_ERROR_PROBABILITY = 0.1

NO_ERROR_PROBABILITY = 0.50
REMOVE_DIACRITICS_PROBABILITY = 0.50
##############################################################################

def apply_keyboard_error(text):

    text_chars = list(text)
    number_of_errors = 0

    for i, char in enumerate(text_chars):
        if char in keyboard_neighbors and random.random() < KEYBOARD_ERROR_PROBABILITY:
            text_chars[i] = random.choice(keyboard_neighbors[char])
            number_of_errors += 1

    return ''.join(text_chars)

##############################################################################

def apply_ordering_error(text):

    text_chars = list(text)
    number_of_errors = 0
    
    for _ in range(len(text_chars)):

        # choose a random index
        i = random.randrange(len(text_chars) - 1)

        if random.random() < ORDERING_ERROR_PROBABILITY:
            # swap it with the next character
            text_chars[i], text_chars[i+1] = text_chars[i+1], text_chars[i]
            number_of_errors += 1

    return ''.join(text_chars)

##############################################################################

def apply_phonetic_error(text):

    text_chars = list(text)

    for i, char in enumerate(text_chars):
        if char in phonetic_mapping and random.random() < PHONETIC_ERROR_PROBABILITY:

            if phonetic_mapping[char]:
                text_chars[i] = random.choice(phonetic_mapping[char])

    return ''.join(text_chars)

##############################################################################

DIACRITIC_CHARS = set("".join(d for d in DIACRITICS if d))

def remove_diacritics(text):
    return ''.join(c for c in text if c not in DIACRITIC_CHARS)

def apply_remove_diacritics_error(text):
    
    mode = random.choice(["letter", "word", "full"])

    if mode == "full":
        return remove_diacritics(text)

    words = text.split()
    new_words = []

    for word in words:
        if mode == "word":
            if random.random() < 0.15:
                new_words.append(remove_diacritics(word))
                continue

            new_words.append(word)
            continue

        if mode == "letter":
            new_word = ''.join(
                c if c not in DIACRITIC_CHARS else '' if random.random() < 0.2 else c
                for c in word
            )
            
            new_words.append(new_word)

    return ' '.join(new_words)


def apply_diacritic_error(text):
    
    if random.random() < REMOVE_DIACRITICS_PROBABILITY:
        return apply_remove_diacritics_error(text)
    
    text_chars = list(text)

    for i, char in enumerate(text_chars):
        if char in diacritic_mapping and random.random() < DIACRITIC_ERROR_PROBABILITY:
            text_chars[i] = random.choice(diacritic_mapping[char])

    return ''.join(text_chars)

##############################################################################

# error functions dictionary by type
error_functions = {
    "speech": [apply_phonetic_error, apply_diacritic_error],
    "typing": [apply_keyboard_error, apply_ordering_error],
    "": [apply_keyboard_error, apply_ordering_error, apply_phonetic_error, apply_diacritic_error]
}

# |=======================================================|
# | Error types (each has it's own probability):          |
# |=======================================================|
# | 1. No errors                                          |
# | 2. Speech errors                                      |
# |   2.1. Phonetic errors                                |
# |  2.2. Diacritic errors                                |
# |       2.2.1. Remove diacritics (full, word, letter)   |
# |       2.2.2. Replace diacritics                       |
# | 3. Typing errors                                      |      
# |   3.1. Keyboard errors                                |
# |   3.2. Ordering errors                                |  
# | 4. All errors combined (speech + typing)              | 
# |=======================================================|

def inject_error(text, error_type=""):
    if not text or len(text) < 2:
        return text
    
    if random.random() < NO_ERROR_PROBABILITY:
        return text
    
    selected_error_functions = error_functions.get(error_type, error_functions[""])
    
    for error_func in selected_error_functions:
        text = error_func(text)

    return text