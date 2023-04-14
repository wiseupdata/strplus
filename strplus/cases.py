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
    words = sum([re.findall(r'[a-zA-Z0-9]+', word) for word in re.sub('([A-Z][a-z]+)', r' \1', re.sub('([A-Z]+)', r' \1', text)).split()], [])

    # Capitalize the first letter of each word except the first word
    capitalized_words = []
    for i, word in enumerate(words):
        if i == 0 and word[0].isdigit():
            capitalized_words.append(str(word[0]))
            word = word[1:]
        capitalized_words.append(word.capitalize())
    
    # Join the words back together to form the CamelCase string
    return ''.join(capitalized_words)


def to_camel(text):
    """
    Convert a string from any case to CamelCase.
    """
    text = text.strip()
    
    if not text:  # If the input string is empty, return an empty string
        return ""
    
    # Split the string into words using regex, split 1
    words = sum([re.findall(r'[a-zA-Z0-9]+', word) for word in re.sub('([A-Z][a-z]+)', r' \1', re.sub('([A-Z]+)', r' \1', text)).split()], [])
    
    # Capitalize the first letter of each word except the first word
    capitalized_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
    
    # Join the words back together to form the CamelCase string
    check_01 = ''.join(capitalized_words)
    
    # Final check
    words = re.split('[-_]', check_01)
    
    return words[0] + ''.join(word.capitalize() for word in words[1:]).replace('_', '')

def to_snake(text):
    """Converts a string to snake_case"""
    text = text.strip()

    if not text:  # If the input string is empty or only whitespace, return an empty string
        return ""

    # Remove any non-alphanumeric characters and split the string into words
    words = sum([re.findall(r'[a-zA-Z0-9]+', word) for word in re.sub('([A-Z][a-z]+)', r'_\1', re.sub('([A-Z]+)', r'_\1', text)).split()], [])

    # Join the words back together to form the snake_case string
    return '_'.join([word.lower() for word in words])


def to_list(text):
    """Converts a string to list"""
    text = text.strip()

    if not text:  # If the input string is empty or only whitespace, return an empty string
        return []

    # Remove any non-alphanumeric characters and split the string into words
    word_list = sum([re.findall(r'[a-zA-Z0-9]+', word) for word in re.sub('([A-Z][a-z]+)', r'_\1', re.sub('([A-Z]+)', r'_\1', text)).split()], [])

    return word_list


