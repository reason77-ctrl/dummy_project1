import pytest
from package_reason.count_str import count_str

# Test case for counting lower case character
def test_count_str():
    assert count_str("some char", "a") == 1
    assert count_str("My name is reason regmi", "r") == 2


# Test case for counting uppercase character
def test_count_str_allCases():
    assert count_str("Hello Hi", "H") == 2


# Test case for counting character not present in string
def test_count_str_notPresent():
    assert count_str("Hello Reason", "x") == 0


# Test case for counting character in an empty string
def test_count_str_emptyStr():
    assert count_str("", "a") == 0


# Test case for counting character in single character string
def test_count_str_singleChar():
    assert count_str("b","b") == 1


# Test case for counting blank space in character
def test_count_str_blank():
    assert count_str("Hello wor ld", " ") == 2


# Test case for counting special characters
def test_count_str_specialChar():
    assert count_str("!@##$%^#", "#") == 3


# Test case for counting string instead of single character
def test_count_str_string_input():
    with pytest.raises(ValueError):
        count_str("hello man", "lo")