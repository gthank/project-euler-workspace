"""
Solves `Problem 25`_ from Project Euler.

.. _Problem 25: http://projecteuler.net/index.php?section=problems&id=25
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
        return term

    return fib(term - 2) + fib(term - 1) 
