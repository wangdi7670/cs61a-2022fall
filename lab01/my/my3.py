def foo(x):
    """A random function.

    >>> foo(4)
    4
    >>> foo(5)
    5
    """
    print("hello, world")
    if x == 4:
        return 4
    else:
        return 505

    return x + 1


print(foo(3))