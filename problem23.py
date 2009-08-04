def _factorize(to_factor):
    """
    Use trial division to _factorize ``to_factor``; return a list of the factors.

    >>> _factorize(220)
    [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    >>> _factorize(12)
    [1, 2, 3, 4, 6]
    """
    factors = [1]
    divisor = 2
    while (divisor < int(to_factor)):
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


# Find all the abundant numbers between 12 and 28123 - 12
# Starting at 28123, count down and find the first number that can be written as the sum of any two numbers from the above list.
