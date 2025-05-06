# lib/testing/test_not_none.py
from not_none_functions import return_not_none

def test_return_not_none():
    assert return_not_none(5) == 'Processed: 5'
    assert return_not_none(None) == None
