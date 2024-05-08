import random
import string
from typing import List, Optional

import nltk

nltk.download('words')


def generate_random_password(length: int = 8, include_numbers: bool = False, include_symbols: bool = False) -> str:
    """
    Generate a random password.
    """
    if include_numbers and include_symbols:
        characters = string.ascii_letters + string.digits + string.punctuation
    elif include_numbers:
        characters = string.ascii_letters + string.digits
    elif include_symbols:
        characters = string.ascii_letters + string.punctuation
    else:
        characters = string.ascii_letters

    return ''.join(random.choice(characters) for _ in range(length))


def generate_memorable_password(
    no_of_words: int = 5,
    separator: str = "-",
    capitalization: bool = False,
    vocabulary: Optional[List[str]] = None
) -> str:
    """
    Generate a memorable password from a list of vocabulary words.
    """
    if vocabulary is None:
        vocabulary = nltk.corpus.words.words()

    password_words = random.sample(vocabulary, no_of_words)

    if capitalization:
        password_words = [word.capitalize() for word in password_words]

    return separator.join(password_words)


def generate_pin(length: int = 4) -> str:
    """
    Generate a numeric pin code.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))
