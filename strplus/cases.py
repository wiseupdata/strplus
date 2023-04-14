import re
import logging
from typing import List

logger = logging.getLogger(__name__)

def to_pascal(input_string):
    """Converts a string to PascalCase"""
    # split string into words
    words = input_string.split()
    # capitalize the first letter of each word and join them
    pascal_case = ''.join([word.capitalize() for word in words])
    return pascal_case

import re

def to_camel(text):
    """
    Convert a string from any case to CamelCase.
    """
    text = text.strip()
    
    if not text:  # If the input string is empty, return an empty string
        return ""
    
    # Remove any underscores or hyphens and split the string into words
    words = re.findall(r'\w+', text)

    # Capitalize the first letter of each word except the first word
    capitalized_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
    
    # Join the words back together to form the CamelCase string
    return ''.join(capitalized_words)


