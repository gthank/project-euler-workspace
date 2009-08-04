"""
Solve `Problem 22`_ from Project Euler.

.. _Problem 22: http://projecteuler.net/index.php?section=problems&id=22
"""


from string import ascii_uppercase


def _massage_names(name_string):
    """
    Extract a list of names from ``name_string``, assuming it's a \
    string where the values are comma-separated and wrapped in ``"`` \
    characters.

    >>> _massage_names('"ANDY","SALLY"')
    ['ANDY', 'SALLY']
    """
    return sorted([name.strip('"') for name in name_string.split(',')])


def _load_names(name_file):
    """Loads the names from ``name_file``, strips the double quotes, \
    and returns a sorted version of that sequence before returning it."""
    names = None
    with open(name_file, 'r') as in_file:
        for line in in_file:
            names = _massage_names(line)
    return names


def _alpha_value(chars):
    """Calculate the alphabetical value (as described by `Problem 22`_).

    .. _Problem 22: http://projecteuler.net/index.php?section=problems&id=22

    >>> _alpha_value('COLIN')
    53
    >>> _alpha_value('RUTH')
    67
    """
    return sum((1 + ascii_uppercase.index(char) for char in chars))


def _score_name_list(name_list):
    """
    For each name in the list, calculate its alphabetical value and \
    multiply by its position in the list.

    >>> _score_name_list(['COLIN', 'RUTH'])
    [53, 134]
    """
    return ((i + 1) * _alpha_value(name) for i, name in enumerate(name_list))


def problem_22():
    """
    Solve `Problem 22`_ and return the numeric answer.

    .. _Problem 22: http://projecteuler.net/index.php?section=problems&id=22
    """
    names = _load_names('names.txt')
    return sum(_score_name_list(names))


if __name__ == '__main__':
    print problem_22()
