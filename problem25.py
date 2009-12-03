"""
Solves `Problem 25`_ from Project Euler.

.. _Problem 25: http://projecteuler.net/index.php?section=problems&id=25
"""
import itertools


def fib():
    """Generator for the Fibonacci sequence."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


def problem_twenty_six():
    """Find the first term in the Fibonacci sequence to contain 1000 digits."""
    fibs = fib()
    big_num = 10**999
    return itertools.dropwhile(lambda x: len(str(x)) < big_num, fibs).next()


if (__name__ == "__main__"):
    print problem_twenty_six()
