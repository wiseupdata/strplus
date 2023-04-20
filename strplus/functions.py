from strplus.cases import *


def get_separator(input_string):
    """get_separator _summary_

    _extended_summary_

    :param input_string: _description_
    :type input_string: _type_
    :return: _description_
    :rtype: _type_
    """
    separators = [",", ";", "|", " ", "\t", ":", "/", "\\", "\n"]

    # check each separator in the order of priority
    for sep in [",", ";", "|", " ", "\t", ":", "/", "\\", "\n"]:
        if sep in input_string:
            sep_count = input_string.count(sep)
            if sep_count == 1:
                return sep
            elif sep_count > 1:
                return max(separators, key=input_string.count)

    # if no separator was found, return None
    return None
