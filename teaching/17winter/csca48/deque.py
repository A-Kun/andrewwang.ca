class EmptyQueueError(Exception):
    '''An error to be raised when someone tries to dequeue from an empty queue.'''


class Deque():
    '''A double ended queue.'''

    def __init__(self: 'Deque') -> None:
        '''
        Initialize this Deque object.
        '''
        # Representation invariant:
        # _contents is a list of object.
        # _contents[:] are the objects in the deque.
        # if i < j, i >=0, j < len(_contents), then
        #    _contents[i] is to the left of _contents[j] in the deque
        #    _contents[j] is to the right of _contents[i] in the deque

        self._contents = []

    def enqueue_left(self: 'Deque', item: 'object') -> None:
        '''
        Add item onto the left side of the deque.
        '''
        self._contents.insert(0, item)

    def enqueue_right(self: 'Deque', item: 'object') -> None:
        '''
        Add item onto the right side of the deque.
        '''
        self._contents.append(item)

    def dequeue_left(self: 'Deque') -> object:
        '''
        Remove and return the leftmost item in the deque.
        '''
        if(self.is_empty()):
            raise EmptyQueueError("Can't dequeue from an empty queue")
        else:
            return self._contents.pop(0)

    def dequeue_right(self: 'Deque') -> object:
        '''
        Remove and return the rightmost item in the deque.
        '''
        if(self.is_empty()):
            raise EmptyQueueError("Can't dequeue from an empty queue")
        else:
            return self._contents.pop()

    def is_empty(self: 'Deque') -> bool:
        '''
        Return True iff this deque is empty.
        '''
        return len(self._contents) == 0


def is_palindrome(word: 'str') -> bool:
    '''
    Return True if word is a palindrome, otherwise return False.
    A palindrome is a word which reads the same backward or forward.

    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("abcabcd")
    False
    >>> is_palindrome("anna")
    True
    >>> is_palindrome("abcd")
    False
    '''
    # Initialize an empty Deque
    my_deque = Deque()
    # Loop through every letter in the word and put them into the Deque
    for next_letter in word:
        my_deque.enqueue_right(next_letter)
    # Initialize a flag indicating if the word is a palindrome
    result = True
    try:
        # Loop though letters in the Deque until it's empty,
        # or already found that the word is not a palindrome
        while not my_deque.is_empty() and result:
            # Check if the letters on both sides are identical
            if my_deque.dequeue_left() != my_deque.dequeue_right():
                # If they are not identical, then the word is not a palindrome
                result = False
    # If there is one last letter left in a word with an odd number of letters,
    # we don't care about the last letter and the word is a palindrome
    except EmptyQueueError:
        result = True
    return result


if(__name__ == "__main__"):
    dq = Deque()
    dq.enqueue_left('A')
    dq.enqueue_left('B')
    dq.enqueue_left('C')
    dq.enqueue_right('D')
    dq.enqueue_right('E')
    dq.enqueue_right('F')
    while not dq.is_empty():
        print(dq.dequeue_right())
        print(dq.dequeue_left())

    print(is_palindrome("anna"))
    print(is_palindrome("racecar"))
    print(is_palindrome("rbc"))
    print(is_palindrome("cibc"))
