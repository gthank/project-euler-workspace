"""Solves Problem 7 from Project Euler."""

import math

FIRST_SIX_PRIMES = {1:2, 2:3, 3:5, 4:7, 5:11, 6:13}

def e_sieve(upper_bound):
    """Uses the Sieve of Eratosthenes to get a list of the primes up to max."""
    primes = []
    candidates = range(2, upper_bound)
    while candidates:
        head = candidates[0]
        primes.append(head)
        candidates = [n for n in candidates[1:] if n % head]

    return primes

# I know it's currently unused, but I wanted to write a generator.
def primes_generator(upper_bound):
    """Uses the Sieve of Eratosthenes behind the scenes to build a \
    generator for prime numbers."""
    candidates = range(2, upper_bound)
    while len(candidates) > 1:
        next_prime = candidates.pop(0)
        candidates = [n for n in candidates if n % next_prime]
        yield next_prime
    yield candidates.pop()

def problem_7(n):
    """Finds the nth prime number.

    Thanks to
    http://en.wikipedia.org/wiki/Prime_number_theorem#Approximations_for_the_nth_prime_number
    we know that it will be less than n * ln(n) + n * ln(ln(n))
    (for n >= 6).
    """
    if n < 6:
        return FIRST_SIX_PRIMES[n]

    upper_bound = int(n * math.log(n) + n * math.log(math.log(n)))

    primes = e_sieve(upper_bound)
    return primes[n - 1]

if __name__ == '__main__':
    print problem_7(10001)
