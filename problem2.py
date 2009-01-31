"""Sums all the even-valued Fibonacci numbers less than 4,000,000.

For more info, see http://projecteuler.net/index.php?section=problems&id=2

"""

def fib(term):
    """Calculate the nth Fibonacci number."""
    if (1 >= term):
        return 1

    return fib(term - 2) + fib(term - 1) 

def problem_two():
    """Calculate the sum of the even Fibonacci numbers less than 4,000,000."""
    # I precalculated the index of the largest Fibonacci number less than
    # 4,000,000 and it was 32.
    fibs = [fib(n) for n in range(33)]
    return sum([cur_fib for cur_fib in fibs if not cur_fib % 2])

if (__name__ == "__main__"):
    print problem_two()

