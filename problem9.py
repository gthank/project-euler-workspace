"""Solves Problem 9 from Project Euler."""

import operator

def triples(upper_bound):
    """Generator for Pythagorean Triples (represented as tuples).

    Uses Euclid's formula to generate Pythagorean Triples
    (see http://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple).
    """
    for m in xrange(2, upper_bound):
        for n in xrange(1, m):
            yield m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2
# Only uncomment if the triples we get from the original Euclid's are insufficient.
# for k in xrange(1, upper_bound):
#     yield k * (m ** 2 - n ** 2), k * (2 * m * n), k * (m ** 2 + n ** 2)
                
def problem_9():
    """Finds the product of the Pythagorean Triple where a + b + c = 1000."""
    for triple in triples(1000):
        if sum(triple) == 1000:
            return reduce(operator.mul, triple)
    return 0

if __name__ == '__main__':
    print problem_9()