"""Solves Problem 6 from Project Euler."""

def sum_of_squares(upper_bound):
    """Sums the squares of all the natural numbers from 1 to \
    upper_bound (inclusive)."""
    # Use the rule for square pyramidal numbers
    # (http://en.wikipedia.org/wiki/Square_pyramidal_number).
    return ((2 * upper_bound ** 3) + (3 * upper_bound ** 2) + upper_bound) / 6

def square_of_sums(upper_bound):
    """Sums all the numbers from 1 to upper_bound."""
    # Use Gauss' insight about n/2 * (n + 1).
    return (upper_bound * (upper_bound + 1) / 2) ** 2

def problem_6(n):
    """Finds the difference between the square of the sums and the \
    sum of the squares for the first n natural numbers."""
    return square_of_sums(n) - sum_of_squares(n)

if __name__ == '__main__':
    print problem_6(100)
