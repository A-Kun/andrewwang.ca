class DLLNode(object):
    """A Node in a doubly-linked list"""

    def __init__(self, data, prev_link=None, next_link=None):
        '''(DLLNode, object, DLLNode, DLLNode) -> NoneType

        Create a new DLLNode containing object, with previous node
        prev_link, and next node next_link.
        '''
        # Representation invariant:
        # data is an object
        # prev_link is a DLLNode
        # next_link is a DLLNode
        # data is the item held in this node
        # if prev_link is None, then
        #     this node is the head of the list
        # if prev_link is not None, then
        #     prev_link is the node immediately before (closer
        #     to the head of the list than) this node
        # if next_link is None, then
        #     this node is the tail of the list
        # if next_link is not None, then
        #     next_link is the node immediately after (closer
        #     to the tail of the list than) this node

        self.data = data
        self.prev_link = prev_link
        self.next_link = next_link

    def __str__(self):
        '''(DLLNode) -> str
        Return a str representation of this DLLNode.
        '''

        return str(self.data)


class DoublyLinkedList(object):
    """A doubly linked list"""

    def __init__(self):
        '''(DoublyLinkedList) -> NoneType
        Create a new empty DoublyLinkedList
        '''
        # Representation invariant:
        # _head is a DLLNode
        # _tail is a DLLNode
        # if the list is empty:
        #     _head = _tail = None
        # if the list is non-empty:
        #     _head is the first node in the list
        #     _tail is the last node in the list
        #     if nodeA and nodeB are both nodes in this list and nodeA is
        #     before (closer to the head than) nodeB:
        #         nodeA.next_link == nodeB
        #         nodeB.prev_link == nodeA
        self._head = None
        self._tail = None

    def add_head(self, add_obj):
        '''(DoublyLinkedList, object) -> NoneType
        Add add_obj to the head of this DoublyLinkedList.
        '''
        new_node = DLLNode(add_obj, None, self._head)
        if self._head is None:
            self._tail = new_node
        else:
            self._head.prev_link = new_node

        self._head = new_node

    def __str__(self):
        '''(DoublyLinkedList) -> str

        Return a str representation of the contents of this
        DoublyLinkedList.
        '''
        result = ""
        curr = self._head
        while curr is not None:
            result += str(curr)
            if curr.next_link is not None:
                result += " -> "
            curr = curr.next_link
        return result

    def add_tail(self, add_obj):
        '''(DoublyLinkedList, object) -> NoneType
        Add add_obj to the tail of this DoublyLinkedList.
        '''
        new_node = DLLNode(add_obj, self._tail, None)
        if self._tail is None:
            self._head = new_node
        else:
            self._tail.next_link = new_node
        self._tail = new_node

    def remove_head(self):
        '''(DoublyLinkedList) -> object
        Remove and return the first item in this DoublyLinkedList.
        '''
        self._head = self._head.next_link
        self._head.prev_link = None

    def remove_tail(self):
        '''(DoublyLinkedList) -> object
        Remove and return the last item in this DoublyLinkedList.
        '''
        self._tail = self._tail.prev_link
        self._tail.next_link = None


if __name__ == '__main__':
    my_dll = DoublyLinkedList()
    my_dll.add_head(1)
    my_dll.add_head(2)
    my_dll.add_head(3)
    my_dll.add_tail(4)
    my_dll.add_tail(5)
    my_dll.add_tail(6)
    my_dll.remove_head()
    my_dll.remove_tail()
    print(my_dll)
