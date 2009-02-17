"""Solves Problem 12 of Project Euler."""

import math

def factors(to_factor):
    """Find the factors of to_factor."""
    factors = []
    divisor = 1
    while (divisor <= int(math.sqrt(to_factor))):
        if not to_factor % divisor:
            quotient = to_factor / divisor
            factors.append(divisor)
            factors.append(quotient)
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
    for triangular in triangular_numbers():
        cur_factors = factors(triangular)
        print cur_factors
        if len(cur_factors) > min_divisors:
            return triangular

if __name__ == '__main__':
    print problem_12(5)
