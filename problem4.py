"""Solves Problem 4 from Project Euler.
"""

def is_palindrome(to_test):
    """Determine whether to_test is a palindrome."""
    # Uses extended slice syntax to reverse a sequence.
    return to_test == to_test[::-1]

def problem_4():
    """Function to solve problem 4."""
    # I arrived at the values in the range by finding the smallest and largest
    # products of 2 3-digit numbers.
    for n in reversed(xrange(10000, 998001)):
        if is_palindrome(str(n)):
            for factor_1 in reversed(xrange(1000)):
                for factor_2 in reversed(xrange(1000)):
                    if n == (factor_2 * factor_1):
                        return n

    return 255  # Return a sentinel value to indicate failure.

if __name__ == '__main__':
    print problem_4()
