class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class PriorityQueueBase:
    """Abstract base class for a priority queue."""

    class _Item:
        """Lightweight composite to store priority queue items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key           # compare items based on their keys

        def is_empty(self):
            """Return True if the priority queue is empty."""
            return len(self) == 0                   # concrete method assuming abstract len

class UnsortedPriorityQueue(PriorityQueueBase):     # base class defines _Item
    """A min-oriented priority queue implemented with an unsorted list."""

    def _find_min(self):            # nonpublic utility
        """Return Position of item with minimum key."""
        if self.is_empty():         # is_empty inherited from base class
            raise Empty('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        """Creratet a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        self._data.add_last(self._Item(key, value))

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key."""
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        p = self._find_min()
        item = self._data.delete(p)
        return(item._key, item._value)

class SortedPriorityQueue(PriorityQueueBase):     # base class defines _Item
    """A min-oriented priority queue implemented with an sorted list."""

    def __init__(self):
        """Creratet a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        newest = self._Item(key, value)         # make new item instance
        walk = self._data.last()                # walk backward looking for smaller key
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk,newes)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key."""
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data.delete(self._data.first())
        return(item._key, item._value)

class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a binary heap."""
#------------------------- nonpublic behaviors ----------------------------------
def _parent(self,j):
    return (j-1)//2

def _left(self, j):
    return 2*j + 1

def _right(self, j):
    return 2*j + 2

def _has_left(self, j):
    return self._left(j) < len(self._data)      # index beyond end of list?

def _has_right(self, j):
    return self._right(j) < len(self._data)      # index beyond end of list?

def _swap(self, i, j):
    """Swap the elements at indices i and j of array."""
    self._data[i], self._data[j] = self._data[j], self._data[i]

def _upheap(self, j):
    parent = self._parent(j)
    if j > 0 and self._data[j] < self._data[parent]:
        self._swap(j, parent)
        self._upheap(parent)                    # recur at position of parent
def _downheap(self, j):
    if self._has_left(j):
        left = self._left(j)
        small_child = left
        if self._has_right(j):
            right = self._right(j)
            if self._data[right] < self._data[left]:
                small_child = right
        if self._data[small_child] < self._data[j]:
            self._swap(j, small_child)
            self._downheap(small_child)         # recur at position of small child

def _heapify(self):
    start = self._parent(len(self) - 1)         # start at PARENT of last leaf
    for j in range(start, -1, -1):              # going to and including the root
        self._downheap(j)

#------------------------- public behaviors ----------------------------------
def __init__(self, contents = ()):
    """Create a new empty Priority Queue.

    By default, queue with be empty. If contents is given, it should be as an iterable sequence
    of (k,v) tuples specifying the initial contents.
    """
    # self._data = []
    self._data = [self._Item(k,v) for k, v in contents]    # empty by default
    if len(self._data) > 1:
        self._heapify()

def __len__(self):
    """Return the number items in the priority queue."""
    return len(self._data)

def add(self, key, value):
    """Add a key-value pair to the priority queue."""
    self._data.append(self._Item(key, value))
    self._uphead(len(self._data)-1)             # upheap newly added position

def min(self):
    """Return but do not remove (k, v) tuple with minimum key.

    Raise Empty exception if empty.
    """

    if self.is_empty():
        raise Empty('Priority queue is empty.')
    self._swap(0, len(self._data)-1)            # put minimum item at the end
    item = self._data.pop()                     # and remove it from the list
    self._downheap(0)                           # then fix new root
    return (item._key, item._value)

