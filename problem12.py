"""Solves Problem 12 of Project Euler."""

import math

def nonprime_factors(to_factor):
    """Find the factors of to_factor."""
    factors = []
    divisor = 1
    while (divisor <= int(math.sqrt(to_factor))):
        if not to_factor % divisor:
            to_factor /= divisor
            factors.append(divisor)
            factors.append(to_factor)
        divisor += 1

    return factors

def triangular_numbers():
    """Generate the triangular numbers."""
    current = 0
    position = 1
    while True:
        current += position
        position += 1
        yield current

def problem_12(min_divisors):
    """Finds the first triangular number to have more than 500 divisors."""
    pass

if __name__ == '__main__':
    print problem_12(500)
