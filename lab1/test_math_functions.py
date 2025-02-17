from math_functions import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(5, 5) == 10

def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(1, 1) == 0
    assert subtract(15, 5) == 10

def test_multiply():
    assert multiply(3, 2) == 6
    assert multiply(1, 1) == 1
    assert multiply(-1, 5) == -5

def test_multiply():
    assert divide(4, 2) == 2
    assert divide(10, 2) == 5
    assert divide(1, -1) == -1