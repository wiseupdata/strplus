from strplus.cases import *

def get_separator(input_string):
    separators = [',', ';', '|', ' ', '\t', ':', '/', '\\', '\n']
    
    # check each separator in the order of priority
    for sep in [',', ';', '|', ' ', '\t', ':', '/', '\\', '\n']:
        if sep in input_string:
            sep_count = input_string.count(sep)
            if sep_count == 1:
                return sep
            elif sep_count > 1:
                return max(separators, key=input_string.count)
    
    # if no separator was found, return None
    return None