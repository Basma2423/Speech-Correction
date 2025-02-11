import random
from src.helping_dictionaries import keyboard_neighbors, phonetic_mapping, diacritic_mapping

KEYBOARD_ERROR_PROBABILITY = 0.02
ORDERING_ERROR_PROBABILITY = 0.02
PHONETIC_ERROR_PROBABILITY = 0.06
DIACRITIC_ERROR_PROBABILITY = 0.06

##############################################################################

def apply_keyboard_error(text):

    text_chars = list(text)
    number_of_errors = 0

    for i, char in enumerate(text_chars):
        if char in keyboard_neighbors and random.random() < KEYBOARD_ERROR_PROBABILITY:
            text_chars[i] = random.choice(keyboard_neighbors[char])
            number_of_errors += 1

    print(f'Number of keyboard errors: {number_of_errors}')
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

    print(f'Number of ordering errors: {number_of_errors}')
    return ''.join(text_chars)

##############################################################################

def apply_phonetic_error(text):

    text_chars = list(text)
    number_of_errors = 0

    for i, char in enumerate(text_chars):
        if char in phonetic_mapping and random.random() < PHONETIC_ERROR_PROBABILITY:

            if phonetic_mapping[char]:
                text_chars[i] = random.choice(phonetic_mapping[char])
                number_of_errors += 1

    print(f'Number of phonetic errors: {number_of_errors}')
    return ''.join(text_chars)

##############################################################################

def apply_diacritic_error(text):
    
    text_chars = list(text)
    number_of_errors = 0

    for i, char in enumerate(text_chars):
        if char in diacritic_mapping and random.random() < DIACRITIC_ERROR_PROBABILITY:
            text_chars[i] = random.choice(diacritic_mapping[char])
            number_of_errors += 1

    print(f'Number of diacritic errors: {number_of_errors}\n')
    return ''.join(text_chars)

##############################################################################

# error functions list
error_functions = [
    apply_keyboard_error,
    apply_ordering_error,
    apply_phonetic_error,
    apply_diacritic_error
]

def inject_error(text):

    if not text or len(text) < 2:
        return text

    for error_func in error_functions:
        text = error_func(text)  # Apply each error function independently

    return text  # Convert back to string
