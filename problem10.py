"""Solves Problem 10 for Project Euler."""
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

def primes_generator(upper_bound):
    """A generator for all the primes < upper_bound."""
    candidates = xrange(2, upper_bound)
    primes = []
    for n in candidates:
        if is_prime(n, primes):
            primes.append(n)
            yield n

def problem_10():
    """Sum the primes less than 2 million."""
    return sum(primes_generator(2000000))

if __name__ == '__main__':
    print problem_10()
