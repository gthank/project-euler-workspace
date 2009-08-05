"""
Solve `Problem 23`_.

.. _Problem 23: http://projecteuler.net/index.php?section=problems&id=23
"""


from math import sqrt
import itertools


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


def problem_23():
    """
    Solve `Problem 23`_.

    .. _Problem 23: http://projecteuler.net/index.php?section=problems&id=23
    """
    # upper_limit = 28124
    upper_limit = 25
    abundant_numbers = [number for number in xrange(1, upper_limit)
                        if is_abundant(number)]
    combos = itertools.combinations(abundant_numbers, 2)
    reflexive_combos = ((number, number) for number in abundant_numbers)
    sums = set((sum(combo) for combo in itertools.chain(combos, reflexive_combos)))
    non_sums = (number for number in xrange(1, upper_limit) if not number in sums)
    return sum(non_sums)


if __name__ == '__main__':
    print problem_23()
