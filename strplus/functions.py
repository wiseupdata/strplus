import re
import logging
from typing import List

logger = logging.getLogger(__name__)

def to_pascal_case(input_string):
    """Converts a string to PascalCase"""
    # split string into words
    words = input_string.split()
    # capitalize the first letter of each word and join them
    pascal_case = ''.join([word.capitalize() for word in words])
    return pascal_case
