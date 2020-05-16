
            self._tail = None                   # queue becomes empty
class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""
    #--------------------- nested _Node class -----------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage

        def __init__(self, element, next):      # initialize node's fields
            self._element = element             # reference to user's element
            self._next = next                   # reference to next node

    #----------------------------stack methods-----------------------------
    def __init__(self):
        """Create an empty stack."""
        self._head = None                       # reference to the head node
        self._size = 0                          # number of stack elements

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head)  # create and link a new node
        self._size += 1

    def top(self):
        """Return (but do no remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._head._element              # top of stack is at head of list

    def pop(self):
        """Remove and return the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty.')
        answer = self._head._element
        self._head = self._head._next           # bypass the former top node
        self._size -= 1
        return answer

class LinkedQueue:
    """FIFO Queue implementation using a singly linked list for storage."""
    #--------------------- nested _Node class -----------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage

        def __init__(self, element, next):      # initialize node's fields
            self._element = element             # reference to user's element
            self._next = next                   # reference to next node

    #----------------------------queue methods-----------------------------
    def __init__(self):
        """Create an empty queue."""
        self._head = None                       # reference to the head node
        self._tail = None                       # reference to the tail node
        self._size = 0                          # number of queue elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def enqueue(self, e):
        """Add element e to the back of the queue."""
        newest = self._Node(e, None)            # node will be new tail node
        if self.is_empty():
            self._head = newest                 # special case: previously empty
        else:
            self._tail._next = newest           # update reference to tail node
        self._tail = newest
        self._size += 1


    def first(self):
        """Return (but do no remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('queue is empty.')
        return self._head._element              # front aligned with head of list

    def dequeue(self):
        """Remove and return the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('queue is empty.')
        answer = self._head._element
        self._head = self._head._next           # bypass the former front node
        self._size -= 1
        if self.is_empty():                     # special case as queue is empty
            self._tail = None                   # removed head had been tail
        return answer


class CircularQueue:
    """Queue implementation using a circularly linked list for storage."""
    #--------------------- nested _Node class -----------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage

        def __init__(self, element, next):      # initialize node's fields
            self._element = element             # reference to user's element
            self._next = next                   # reference to next node

    #----------------------------queue methods-----------------------------
    def __init__(self):
        """Create an empty queue."""
        self._tail = None                       # reference to the tail node
        self._size = 0                          # number of queue elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do no remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('queue is empty.')
        head = self._tail._next
        return head._element              # front aligned with head of list

    def enqueue(self, e):
        """Add element e to the back of the queue."""
        newest = self._Node(e, None)            # node will be new tail node
        if self.is_empty():
            newest._next = newest               # initialize circularly
        else:
            newest._next = self._tail._next     # new node points to head
            self._tail._next = newest           # old tails points to new node
        self._size += 1
        self._tail = newest                     # new node becomes the tail

    def dequeue(self):
        """Remove and return the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('queue is empty.')
        oldhead = self._tail._next
        if self._size == 1:                     # removing only element
            self._tail = None                   # queue becomes empty
        else:
            self._tail._next = oldhead._next    # bypass the old head
        self._size -= 1
        return oldhead._element

    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size < 0:
            self._tail = self._tail._next       # old head becomes new tail





