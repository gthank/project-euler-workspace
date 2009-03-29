import math

def sum_of_digits(num):
    """
    Finds the sum of the digits in num (presumed to be base-10).

    >>> sum_of_digits(2 ** 15)
    26
    """
    running_total = 0
    for n in xrange(int(math.log10(num) + 1)):
        running_total += num % 10
        num //= 10
    return running_total

def problem_16():
    """Solves Problem 16 at Project Euler."""
    return sum_of_digits(2 ** 1000)

if __name__ == '__main__':
    print problem_16()