"""Sums all the even-valued Fibonacci numbers less than 4,000,000.

For more info, see http://projecteuler.net/index.php?section=problems&id=2

"""

# Taken from the Python Decorator Library
class memoized(object):
    """Decorator that caches a function's return value each time it is called.

    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    """
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            self.cache[args] = value = self.func(*args)
            return value
        except TypeError:
            # uncachable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args)
    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__

@memoized
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

