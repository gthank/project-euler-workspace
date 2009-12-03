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
