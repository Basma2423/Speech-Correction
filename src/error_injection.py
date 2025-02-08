import random
from src.helping_dictionaries import keyboard_neighbors, phonetic_mapping, diacritic_mapping

KEYBOARD_ERROR_PROBABILITY = 0.04
ORDERING_ERROR_PROBABILITY = 0.04
PHONETIC_ERROR_PROBABILITY = 0.06
DIACRITIC_ERROR_PROBABILITY = 0.06


##############################################################################

def apply_keyboard_error(text):

    text_chars = list(text)

    for i, char in enumerate(text_chars):
        if char in keyboard_neighbors and random.random() < KEYBOARD_ERROR_PROBABILITY:
            text_chars[i] = random.choice(keyboard_neighbors[char])
            print('keyboard error:', char, '->', text_chars[i])
    return ''.join(text_chars)

##############################################################################

def apply_ordering_error(text):
    text_chars = list(text)

    if len(text_chars) < 2:
        return text
    
    # choose a random index
    i = random.randrange(len(text_chars) - 1)

    if random.random() < ORDERING_ERROR_PROBABILITY:
        # swap the characters at the random index and the next index
        text_chars[i], text_chars[i+1] = text_chars[i+1], text_chars[i]

    return ''.join(text_chars)

##############################################################################

def apply_phonetic_error(text):
    text_chars = list(text)

    for i, char in enumerate(text_chars):
        if char in phonetic_mapping and random.random() < PHONETIC_ERROR_PROBABILITY:
            text_chars[i] = random.choice(phonetic_mapping[char])

    return ''.join(text_chars)

##############################################################################

def apply_diacritic_error(text, error_probability=0.04):
    text_chars = list(text)

    for i, char in enumerate(text_chars):
        if char in diacritic_mapping and random.random() < DIACRITIC_ERROR_PROBABILITY:
            text_chars[i] = random.choice(diacritic_mapping[char])
    return ''.join(text_chars)

##############################################################################

def apply_errors_to_segment(text, error_funcs, error_probability=0.04):

    if not text:
        return text

    # random starting index
    start = random.randint(0, len(text) - 1)
    
    # segment length: 1 character ~ 30% of the text length
    segment_length = max(3, int(0.6 * len(text)))
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
    # apply_ordering_error,
    # apply_phonetic_error,
    apply_diacritic_error
]

def inject_error(text, error_probability=0.04):
    return apply_errors_to_segment(text, error_functions, error_probability)