"""Solves Problem 3 from Project Euler."""

import math

def e_sieve(upper_bound):
    """Uses the Sieve of Eratosthenes to get a list of the primes up to max."""
    primes = []
    candidates = range(2, upper_bound)
    while candidates:
        head = candidates[0]
        primes.append(head)
        candidates = [n for n in candidates[1:] if n % head]

    return primes

def find_highest_prime_factor(to_factor):
    """Find the highest prime factor of to_factor."""
    # TODO primality check on to_factor before we calculate the primes
    primes = e_sieve(int(math.sqrt(to_factor)))
    for prime in primes:
        if not to_factor % prime:
            return to_factor / prime

if (__name__ == "__main__"):
    print find_highest_prime_factor(600851475143)

