"""Solves Problem 5 of Project Euler."""

def factorize(to_factor):
    """Use trial division to factorize to_factor and return all the resulting \
    factors."""
    factors = []
    divisor = 2
    while (divisor < to_factor):
        if not to_factor % divisor:
            to_factor /= divisor
            factors.append(divisor)
            # Note we don't bump the divisor here; if we did, we'd have
            # non-prime factors.
        elif divisor == 2:
            divisor += 1
        else:
            # Trivial optimization: skip even numbers that aren't 2.
            divisor += 2
    if not to_factor % divisor:
        # Don't forget the last factor
        factors.append(to_factor)
    return factors

def lcm(numbers):
    """Finds the Least Common Multiple of numbers."""
    highest_degree_factors = {}
    for number in numbers:
        degrees_by_factor = {}
        for factor in factorize(number):
            # Translate the raw list of factors into a dictionary of degrees
            # keyed on the factor.
            current_degree = degrees_by_factor.setdefault(factor, 0)
            degrees_by_factor[factor] = 1 + current_degree

        # Update the top-level dict so it really is tracking the highest
        # degrees.
        for k, v in degrees_by_factor.iteritems():
            highest_degree_factors.setdefault(k, v)
            if highest_degree_factors[k] < v:
               highest_degree_factors[k] = v 

    running_product = 1
    for factor, degree in highest_degree_factors.iteritems():
        running_product *= factor ** degree

    return running_product

if __name__ == '__main__':
    # Basic idea: factor the numbers; reduce to a tuple for each atom so [2, 2, 3] -> [(2,2), (3,1)]
    # Multiply the unique factors together using the highest degree
    print lcm(range(1,20))
