import math


def factorize(to_factor):
    """
    Use trial division to factorize ``to_factor``; return a list of the factors.

    >>> factorize(220)
    [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    """
    factors = [1]
    divisor = 2
    while (divisor < int(math.sqrt(to_factor))):
        if not to_factor % divisor:
            factors.extend((divisor, to_factor / divisor))
            # Note we don't bump the divisor here; if we did, we'd have
            # non-prime factors.
        divisor += 1
    return sorted(factors)


def main():
    """
    Solve `Problem 21`_ from Project Euler.

    .. _`Problem 21`: http://projecteuler.net/index.php?section=problems&id=21
    """
    amicable_numbers = []
    sums = {}
    for x in xrange(10000):
        sums[x] = sum(factorize(x))
    amicable_numbers = [sum_of_factors for sum_of_factors in sums.values() if sum_of_factors in sums]
    return sum(amicable_numbers)


if __name__ == '__main__':
    print main()
