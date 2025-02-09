import random
from src.helping_dictionaries import keyboard_neighbors, phonetic_mapping, diacritic_mapping

KEYBOARD_ERROR_PROBABILITY = 0.04
ORDERING_ERROR_PROBABILITY = 0.04
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

    print('Number of keyboard errors:', number_of_errors)
    return ''.join(text_chars)

##############################################################################

def apply_ordering_error(text):

    text_chars = list(text)
    number_of_errors = 0

    if len(text_chars) < 2:
        return text
    
    for _ in range(len(text_chars) // 10):
        # choose a random index
        i = random.randrange(len(text_chars) - 1)

        if random.random() < ORDERING_ERROR_PROBABILITY:
            # swap the characters at the random index and the next index
            text_chars[i], text_chars[i+1] = text_chars[i+1], text_chars[i]
            number_of_errors += 1

    print('Number of ordering errors:', number_of_errors)
    return ''.join(text_chars)

##############################################################################

def apply_phonetic_error(text):

    text_chars = list(text)
    number_of_errors = 0

    for i, char in enumerate(text_chars):
        if char in phonetic_mapping and random.random() < PHONETIC_ERROR_PROBABILITY:
            text_chars[i] = random.choice(phonetic_mapping[char])
            number_of_errors += 1

    print('Number of phoentic errors:', number_of_errors)
    return ''.join(text_chars)

##############################################################################

def apply_diacritic_error(text):
    
    text_chars = list(text)
    number_of_errors = 0

    for i, char in enumerate(text_chars):
        if char in diacritic_mapping and random.random() < DIACRITIC_ERROR_PROBABILITY:
            text_chars[i] = random.choice(diacritic_mapping[char])
            number_of_errors += 1

    print('Number of diacritic errors:', number_of_errors)
    return ''.join(text_chars)

##############################################################################

def apply_errors_to_segment(text, error_funcs):

    if not text:
        return text

    # random starting index
    start = random.randint(0, len(text) - 1)
    
    # segment length: 1 character ~ 60% of the text length
    segment_length = max(5, int(0.6 * len(text)))
    end = min(len(text), start + segment_length)
    
    # Extract the segment to modify
    segment = text[start:end]
    
    # Apply each error function to the segment
    for func in error_funcs:
        print('\nsegment before:', segment)
        segment = func(segment)
        print('\nsegment after:', segment)
    
    return text[:start] + segment + text[end:]

##############################################################################

# error functions list
error_functions = [
    apply_keyboard_error,
    apply_ordering_error,
    apply_phonetic_error,
    apply_diacritic_error
]

def inject_error(text):
    text_chars = list(text)  # Convert text to a list for modification

    for error_func in error_functions:
        text_chars = error_func(text_chars)  # Apply each error function independently

    return ''.join(text_chars)  # Convert back to string