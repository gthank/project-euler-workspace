"""Solves Problem 3 from Project Euler."""

def e_sieve(upper_bound):
    """Uses the Sieve of Eratosthenes to get a list of the primes up to max."""
    return _e_sieve_helper([], range(2, upper_bound))

def _e_sieve_helper(primes, candidates):
    """Find the primes in candidates using the Sieve of Eratosthenes."""
    if not candidates:
        return primes

    head = candidates[0]
    primes.append(head)
    candidates = [n for n in candidates[1:] if n % head]
    return _e_sieve_helper(primes, candidates)

def find_highest_prime_factor(to_factor):
    """Find the highest prime factor of to_factor."""
    # TODO primality check on to_factor before we calculate the primes
    descending_primes = e_sieve(to_factor).reverse()
    for prime in descending_primes:
        if not to_factor % prime:
            return prime

if (__name__ == "__main__"):
    print find_highest_prime_factor(600851475143)

