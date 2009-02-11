"""Solves Problem 9 from Project Euler."""

import operator

def triplets():
    """Generator for Pythagorean Triples (represented as tuples).

    Uses Euclid's formula to generate Pythagorean Triples
    (see http://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple)."""
    m = 2
    n = 1
    while True:
        yield m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2
        m += 1
        n += 1

def problem_9():
    """Finds the product of the Pythagorean Triple where a + b + c = 1000."""
    for triplet in triplets():
        if sum(triplet) == 1000:
            return reduce(operator.mul, triplet)
        elif sum(triplet) > 1000:
            break
    return 0

if __name__ == '__main__':
    print problem_9()