def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    pass


def divide(x, y):
    if y == 0:
        raise ValueError("cannot divide by zero")
    return x / y
