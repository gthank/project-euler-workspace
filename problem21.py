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
    amicable_numbers = set()
    for x in xrange(10000):
        y = sum(factorize(x))
        if x != y and x == sum(factorize(y)):
            amicable_numbers.add(x)
            amicable_numbers.add(y)
    return sum(amicable_numbers)


if __name__ == '__main__':
    print main()
