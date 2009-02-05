"""Solves Problem 6 from Project Euler."""

def sum_of_squares(upper_bound):
    """Sums the squares of all the natural numbers from 1 to \
    upper_bound."""
    return sum(n ** 2 for n in range(1, upper_bound))

def square_of_sums(upper_bound):
    """Sums all the numbers from 1 to upper_bound."""
    # Use Euler's insight about n/2 * (n + 1).
    return (upper_bound * (upper_bound + 1) / 2) ** 2

def problem_6(n):
    """Finds the difference between the square of the sums and the \
    sum of the squares for the first n natural numbers."""
    return square_of_sums(n) - sum_of_squares(n)

if __name__ == '__main__':
    print problem_6(10)
