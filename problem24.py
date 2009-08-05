"""
Solve `Problem 24`_.

.. _Problem 24: http://projecteuler.net/index.php?section=problems&id=24
"""


import itertools


def problem_24(sequence, desired_permutation):
    """
    Solve `Problem 24`_.

    .. _Problem 24: http://projecteuler.net/index.php?section=problems&id=24

    >>> problem_24([0,1,2], 3)
    102
    """
    str_sequence = (str(foo) for foo in sequence)
    str_perms = itertools.permutations(str_sequence)
    sorted_perms = sorted(int(''.join(perm)) for perm in str_perms)
    return sorted_perms[desired_permutation - 1]


if __name__ == '__main__':
    print problem_24(xrange(0, 10), 1000000)
