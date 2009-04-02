import re

ONES = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
TENS = ["ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDREDS = ["hundred"]
THOUSANDS = ["thousand"]
CHARACTERS_WE_CARE_ABOUT = re.compile("\w")

def _words_from_num(num):
    """
    Convert ``num`` to its (British) English phrase equivalent.
    
    >>> _words_from_num(115)
    'one hundred and fifteen'
    """
    # FIXME
    return str(num)

def _count_characters_we_care_about(string_to_count):
    """
    Count the characters in ``string_to_count``, excluding things like hyphens and spaces.
    
    >>> _count_characters_we_care_about("one hundred and fifteen")
    20
    """
    return len(CHARACTERS_WE_CARE_ABOUT.findall(string_to_count))

def problem_17(upper_bound = 1001):
    """
    Find the solution to `Problem 17`_ at `Project Euler`_.
    
    .. _Problem 17: http://projecteuler.net/index.php?section=problems&id=17
    .. _Project Euler: http://projecteuler.net/
    
    >>> problem_17(2)
    'six'
    """
    converted_nums = [_words_from_num(num) for num in range(1, upper_bound)]
    lengths = [_count_characters_we_care_about(phrase) for phrase in converted_nums]
    return sum(lengths)

if __name__ == '__main__':
    problem_17()