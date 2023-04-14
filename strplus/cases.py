import re
import logging
from typing import List

logger = logging.getLogger(__name__)

def to_pascal(text):
    """Converts a string to PascalCase"""
    text = text.strip()
    
    if not text:  # If the input string is empty or only whitespace, return an empty string
        return ""
    
    # Remove any underscores, hyphens, or spaces and split the string into words
    words = re.findall(r'[a-zA-Z0-9]+', text)

    # Capitalize the first letter of each word except the first word
    capitalized_words = []
    for i, word in enumerate(words):
        if i == 0 and word[0].isdigit():
            capitalized_words.append(str(word[0]))
            word = word[1:]
        capitalized_words.append(word.capitalize())
    
    # Join the words back together to form the CamelCase string
    return ''.join(capitalized_words)

import re

def to_camel(text):
    """
    Convert a string from any case to CamelCase.
    """
    text = text.strip()
    
    if not text:  # If the input string is empty or only whitespace, return an empty string
        return ""
    
    # Remove any underscores, hyphens, or spaces and split the string into words
    words = re.findall(r'[a-zA-Z0-9]+', text)

    # Capitalize the first letter of each word except the first word
    capitalized_words = []
    for i, word in enumerate(words):
        if i == 0 and word[0].isdigit():
            capitalized_words.append(str(word[0]))
            word = word[1:]
        capitalized_words.append(word.capitalize())
    
    # Join the words back together to form the CamelCase string
    return ''.join(capitalized_words)





