def find_max_sum(triangle):
    """
    Find the maximum sum for a path from the top to the bottom of ``triangle``.

    >>> test = [[3,], \
            [7, 5], \
            [2, 4, 6], \
            [8, 5, 9, 3]]
    >>> find_max_sum(test)
    23
    """
    while len(triangle) > 1:
        _reduce_triangle(triangle)
    return triangle[0][0]


def _reduce_triangle(to_reduce):
    """
    Reduce ``to_reduce`` in place by rolling up the maximum path info one row.

    Don't return anything to emphasize the in-place nature of this function.

    >>> test = [[3,], \
            [7, 5], \
            [2, 4, 6], \
            [8, 5, 9, 3]]
    >>> _reduce_triangle(test)
    >>> test
    [[3], [7, 5], [10, 13, 15]]
    >>> _reduce_triangle(test)
    >>> test
    [[3], [20, 20]]
    >>> _reduce_triangle(test)
    >>> test
    [[23]]
    """
    last_row = to_reduce[-1]
    for index in xrange(len(to_reduce) - 1):
        to_reduce[-2][index] += max(last_row[index:index + 2])
    del to_reduce[-1]


def _parse_triangle_from_file(data_file):
    """
    Parse out the triangle data from ``data_file``.

    >>> _parse_triangle_from_file('test_triangle.txt')
    [[3], [7, 5], [10, 13, 15]]
    """
    triangle = []
    with open(data_file, 'r') as triangle_file:
        for line in triangle_file:
            triangle.append([int(x) for x in line.split()])
    return triangle


def main():
    """
    Solve `Problem 67`_ of Project Euler.

    .. _Problem 67: http://projecteuler.net/index.php?section=problems&id=67
    """
    print find_max_sum(_parse_triangle_from_file('triangle.txt'))


if __name__ == '__main__':
    main()
