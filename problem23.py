"""
Solve `Problem 23`_.

.. _Problem 23: http://projecteuler.net/index.php?section=problems&id=23
"""


from math import sqrt


def _factorize(to_factor):
    """
    Use trial division to factorize ``to_factor``; return a list of the factors.

    >>> _factorize(220)
    [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    >>> _factorize(12)
    [1, 2, 3, 4, 6]
    """
    factors = [1]
    divisor = 2
    last_number = int(sqrt(to_factor))
    while (divisor <= last_number):
        if not to_factor % divisor:
            factors.extend((divisor, to_factor / divisor))
        divisor += 1
    return sorted(set(factors))


def _sum_of_factors(number):
    """
    Calculate the sum of the factors of ``number``.

    >>> _sum_of_factors(12)
    16
    """
    return sum(_factorize(number))


def is_abundant(number):
    """
    Determine whether ``number`` is abundant.

    >>> is_abundant(2)
    False
    >>> is_abundant(12)
    True
    """
    return _sum_of_factors(number) > number


def is_sum_of_two_abundants(number):
    """Determines whether ``number`` can be calculated by adding two \
    abundant numbers."""
    # FIXME Precalculate the sums so it's not doing the same work over and over.
    for abundant in ABUNDANTS:
        if (number - abundant) in ABUNDANTS:
            return True
    return False


def problem_23():
    """
    Solve `Problem 23`_.

    .. _Problem 23: http://projecteuler.net/index.php?section=problems&id=23
    """
    return sum((number for number in xrange(1, 28124)
                if not is_sum_of_two_abundants(number)))


# The upper limit and lower limits come from the problem definition.
ABUNDANTS = [number for number in xrange(12, 28123) if is_abundant(number)]

if __name__ == '__main__':
    print problem_23()
