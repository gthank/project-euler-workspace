from datetime import date


def next_first_of_month_in_20th():
    """Generator to list every first of the month during the 20th century."""
    first = date(1901, 1, 1)
    yield first
    while first.year < 2001:
        if first.month == 12:
            first = first.replace(year=first.year + 1)
            first = first.replace(month=1)
        else:
            first = first.replace(month=first.month + 1)
        yield first


def main():
    """
    Solve `Problem 19`_ from Project Euler.
    
    .. _`Problem 19`: http://projecteuler.net/index.php?section=problems&id=19
    """
    return len([first for first in next_first_of_month_in_20th() if first.weekday() == 6])


if __name__ == '__main__':
    print main()
