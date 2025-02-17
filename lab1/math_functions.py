def add(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return "Both inputs must be numbers."
    return x + y

def subtract(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return "Both inputs must be numbers."
    return x - y

def multiply(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return "Both inputs must be numbers."
    return x * y

def divide(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return "Both inputs must be numbers."
    if y == 0:
        return "Cannot divide by zero."
    return x / y