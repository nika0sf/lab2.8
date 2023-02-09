from math import prod


def foo():
    return prod(iter(lambda: int(input()), 0))


result = foo()
print(result)