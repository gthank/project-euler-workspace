"""Finds the solution to Problem 1 from Project Euler.

For more details, see http://projecteuler.net/index.php?section=problems&id=1

"""

def problem_one():
    """Sum the natural numbers less than 1000 that are multiples of 3 or 5."""
    return sum([n for n in range(999) if ((0 == n % 3) or (0 == n % 5))])
    

if (__name__ == "__main__"):
    print problem_one()

