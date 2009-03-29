import math
import operator

def pure_numeric_sum_of_digits(num):
    """
    Finds the sum of the digits in num (presumed to be base-10).

    This version of the method operates purely on numbers.

    >>> pure_numeric_sum_of_digits(2 ** 15)
    26
    """
    running_total = 0
    for n in xrange(int(math.log10(num)) + 1):
        running_total += num % 10
        num //= 10
    return running_total

def string_based_sum_of_digits(num):
    """
    Finds the sum of the digits in num (presumed to be base-10).

    This version of the method works by using a string representation
    of num and converting individual characters to numbers so we can
    operate on it as a sequence.

    >>> string_based_sum_of_digits(2 ** 15)
    26
    """
    digits = [int(digit) for digit in str(num)]
    return reduce(operator.add, digits, 0)    

def problem_16():
    """Solves Problem 16 at Project Euler."""
    return pure_numeric_sum_of_digits(2 ** 1000)

if __name__ == '__main__':
    print problem_16()
