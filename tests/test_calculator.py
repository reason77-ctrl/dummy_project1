def test_addition_int():
    data = [1,2,3]
    result = sum(data)
    assert result == 6

def test_sub():
    a = 5
    b = 3
    result = a-b
    assert result == 2

def test_multiply():
    a = 5
    b = 3
    result = a*b
    assert result == 15

def test_divide():
    a = 10
    b = 2
    result = a/b
    assert result == 5