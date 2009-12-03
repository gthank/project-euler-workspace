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


def problem_twenty_five(num_of_digits):
    """
    Find the first term in the Fibonacci sequence to contain ``num_of_digits`` digits.

    >>> problem_twenty_five(3)
    12
    """
    enumerated_fibs = enumerate(fib())
    return itertools.dropwhile(lambda x: len(str(x[1])) < num_of_digits , enumerated_fibs).next()[0]


if (__name__ == "__main__"):
    print problem_twenty_five(1000)
