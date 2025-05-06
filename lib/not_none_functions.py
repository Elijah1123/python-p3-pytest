# lib/not_none_functions.py
from not_none_functions_helpers import your_function

def return_not_none(value):
    if value is not None:
        return your_function(value)
    return None
