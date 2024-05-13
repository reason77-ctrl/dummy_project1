import pytest
from package_reason.is_primeNum import isPrime


# Test case for Prime Numbers
@pytest.mark.parametrize("num", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
def test_isPrime_prime_num(num):
    assert isPrime(num) is True

# Test case for non-prime Numbers
@pytest.mark.parametrize("num", [1, 4, 6, 8, 9, 10, 12, 14, 15, 20])
def test_isPrime_non_prime_num(num):
    assert isPrime(num) == False

# Test case for edge cases
@pytest.mark.parametrize("num", [0, -1, -2, -3])
def test_isPrime_edge_cases(num):
    assert isPrime(num) == False


# Test case for large prime number
def test_isPrime_large_prime_number():
    assert isPrime(104729) is True