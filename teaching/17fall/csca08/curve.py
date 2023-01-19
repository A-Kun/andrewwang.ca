import math


def mark_adjustment(original):
    '''(float) -> int
    Return the adjusted mark given the
    original mark. Marks are adjusted by
    taking the square root of original
    mark, multiplied by 10, then round
    up.
    >>> mark_adjustment(9)
    30
    >>> mark_adjustment(16)
    40
    >>> mark_adjustment(4)
    20
    '''
    # Take the square root
    adjusted = math.sqrt(original)
    # Multiply by 10
    adjusted = adjusted * 10
    # Round up
    adjusted = math.ceil(adjusted)
    return adjusted

print(__name__)
if __name__ == '__main__':
    print(mark_adjustment(16))
