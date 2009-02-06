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

def problem_7(n):
    """Finds the nth prime number.

    Thanks to
    http://en.wikipedia.org/wiki/Prime_number_theorem#Approximations_for_the_nth_prime_number
    we know that it will be less than n * ln(n) + n * ln(ln(n))
    (for n >= 6).
    """
    if n < 6:
        return FIRST_SIX_PRIMES[n]

    upper_bound = n * math.log(n) + n * math.log(math.log(n))

    primes = e_sieve(upper_bound)

    return "Trying to find the {0} prime. We think it's less than {1}; in fact, we think it's {2}."\
           .format(n, upper_bound, max(primes))

if __name__ == '__main__':
    print problem_7(10001)
