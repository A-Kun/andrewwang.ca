from my_stacks import Stack


class Queue:
    def __init__(self):
        '''(Queue) -> NoneType
        Initialize this Queue object.
        '''
        self._contents = []

    def enqueue(self, new_obj):
        '''(Queue, object) -> NoneType
        Put new_obj into this queue.
        '''
        self._contents.append(new_obj)

    def dequeue(self):
        '''(Queue) -> object
        Return and remove the next object in the queue.
        '''
        return self._contents.pop(0)

    def is_empty(self):
        '''(Queue) -> bool
        Return True if this queue is empty,
        otherwise return False.
        '''
        return len(self._contents) == 0


class QueueB:
    def __init__(self):
        '''(Queue) -> NoneType
        Initialize this Queue object.
        '''
        self._contents = Stack()

    def enqueue(self, new_obj):
        '''(Queue, object) -> NoneType
        Put new_obj into this queue.
        '''
        self._contents.push(new_obj)

    def dequeue(self):
        '''(Queue) -> object
        Return and remove the next object in the queue.
        '''
        temp_stack = Stack()
        while not self._contents.is_empty():
            temp_stack.push(self._contents.pop())
        result = temp_stack.pop()
        while not temp_stack.is_empty():
            self._contents.push(temp_stack.pop())
        return result

    def is_empty(self):
        '''(Queue) -> bool
        Return True if this queue is empty,
        otherwise return False.
        '''
        return self._contents.is_empty()


if __name__ == '__main__':
    my_queue = QueueB()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.is_empty())
