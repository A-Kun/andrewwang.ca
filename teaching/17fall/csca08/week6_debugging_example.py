def every_third(L):
    '''
    (list) -> list
    Return a list containing every third element in L,
    starting at index 0.

    >>> every_third([])
    []
    >>> every_third([0, 1])
    [0]
    >>> every_third([0, 1, 2, 3])
    [0, 3]
    '''
    count = 0
    result = []
    while (count < len(L)):
        if count % 3 == 0:
            result.append(L[count])
    return result


if __name__ == '__main__':
    print(every_third([0, 1, 2, 3]))
