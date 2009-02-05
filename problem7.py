"""Solves Problem 7 from Project Euler."""

def problem_7(n):
    """Finds the nth prime number.

    Thanks to
    http://en.wikipedia.org/wiki/Prime_number_theorem#Approximations_for_the_nth_prime_number
    we know that it will be less than n * ln(n) + n * ln(ln(n))
    (for n >= 6).
    """
    return "Trying to find the {0} prime.".format(n)

if __name__ == '__main__':
    print problem_7(10001)
