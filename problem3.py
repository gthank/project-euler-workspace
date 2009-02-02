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
    highest_prime = None
    primes = e_sieve(int(math.sqrt(to_factor)))
    for prime in primes:
        if not to_factor % prime:
            quotient = to_factor / prime
            if quotient in primes:
                return quotient
            highest_prime = prime

    if highest_prime:
        return highest_prime

    return to_factor

def _factorize(to_factor):
    factors = []
    divisor = 2
    while (divisor < to_factor):
        if not to_factor % divisor:
            to_factor /= divisor
            factors.append(divisor)
        elif divisor == 2:
            divisor += 1
        else:
            divisor += 2
    if not to_factor % divisor:
        factors.append(to_factor)
    return factors

if __name__ == "__main__":
    print max(_factorize(600851475143))

