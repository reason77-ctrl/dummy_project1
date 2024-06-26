import pytest
from package_reason.count_character import charCount

# Test case for counting character in a string without spaces
def test_charCount():
    assert charCount("reason") == {'r':1, 'e':1, 'a':1, 's':1, 'o':1, 'n':1}


# Test case for counting character in a string with spaces
def test_charCount_withSpace():
    assert charCount("rea son") == {'r':1, 'e':1, 'a':1, ' ':1, 's':1, 'o':1, 'n':1}


# Test case for counting character in empty string
def test_charCount_emptyStr():
    assert charCount("") == {}


# Test case for counting special character in a string
def test_charCount_specialChar():
    assert charCount("!!@@$#$%^") == {"!":2, "@":2, "$":2, "#":1, "%":1, "^":1}