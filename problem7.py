"""Solves Problem 7 from Project Euler."""

import math
import sys

def is_prime(candidate, known_primes):
    """Determines whether candidate is prime by trial division using \
    known_primes.

    For this function to work, known_primes *must* be accurate.
    """
    last_possible = math.sqrt(candidate)
    for current_prime in known_primes:
        if current_prime > last_possible:
            break
        if not candidate % current_prime:
            return False
    return True

def primes_generator():
    """A generator for all the primes <= sys.maxint."""
    candidates = xrange(2, sys.maxint)
    primes = []
    for n in candidates:
        if is_prime(n, primes):
            primes.append(n)
            yield n

def problem_7(n):
    """Finds the nth prime number."""
    primes = primes_generator()
    i = 0
    while i < n - 1:
        i += 1
        primes.next()

    return primes.next()

if __name__ == '__main__':
    print problem_7(10001)
