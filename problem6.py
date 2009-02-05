"""Solves Problem 6 from Project Euler."""

def sum_of_squares(upper_bound):
    """Sums the squares of all the natural numbers from 1 to upper_bound."""
    return sum(n ** 2 for n in range(1, upper_bound))

def square_of_sums(upper_bound):
    """Sums all the numbers from 1 to upper_bound."""
    return (upper_bound * (upper_bound + 1) / 2) ** 2