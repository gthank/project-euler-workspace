def find_max_sum(triangle, row=0, col=0):
    """
    Find the maximum sum for a path from the top to the bottom of ``triangle``.

    >>> test = ((3,), \
            (7, 5), \
            (2, 4, 6), \
            (8, 5, 9, 3))
    >>> find_max_sum(test)
    23
    """
    # Greedy salesman is the wrong way to go, but it'll do to POC my 'data structure'.
    if len(triangle) == row + 1:
        return triangle[row][col]
    if triangle[row + 1][col] > triangle[row + 1][col + 1]:
        return triangle[row][col] + find_max_sum(triangle, row + 1, col)
    return triangle[row][col] + find_max_sum(triangle, row + 1, col + 1)


def main():
    """
    Solve `Problem 18`_ of Project Euler.

    .. _Problem 18: http://projecteuler.net/index.php?section=problems&id=18
    """
    actual = ((75,),
             (95, 64),
             (17, 47, 82),
             (18, 35, 87, 10),
             (20, 4, 82, 47, 65),
             (19, 1, 23, 75, 3, 34),
             (88, 2, 77, 73, 7, 63, 67),
             (99, 65, 4, 28, 6, 16, 70, 92),
             (41, 41, 26, 56, 83, 40, 80, 70, 33),
             (41, 48, 72, 33, 47, 32, 37, 16, 94, 29),
             (53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14),
             (70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57),
             (91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48),
             (63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31),
             (4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23))
    print find_max_sum(actual)


if __name__ == '__main__':
    main()
