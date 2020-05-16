import ctypes

class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0                                 # count actual elements
        self._capacity = 0                          # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self,k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index.')
        return self._A[k]

    def append(self, obj):
        """Add object to the end of the array."""
        if self._n == self._capacity:               # not enough space
            self._resize(2 * self._capacity)        # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):                           # nonpublic utility function
        """Resize internal array to capacity c."""
        B = self._make_array(c)                     # new bigger array
        for k in range(self._n):                    # copy to new array
            B[k] = self._A[k]
        self._A = B                                 # use new array
        self._capacity = c

    def _make_array(self,c):                        # nonpublic utility
        """REturn new array with capacity c."""
        return (c * ctypes.py_object())()

    def insert(self, k, value):
        """Insert a value at index k, shifting subsequent values rightward."""
        # for simplicity we assume 0 <= k <= n in this version
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]
        self._A[j] == self._A[j-1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        """REmove first occurence of value (or raise ValueError)."""
        # for simplicity, we do not consider shrink the dynamic array in this version.
        for k in range(self._n):
            if self._A[k] == value:                     # found a match
                for j in range(k, self._n, -1):         # shift others to fill gap
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None             # help garbage collection
                self._n -= 1                            # we have one less item
                return                                  # exit immediately
            raise ValueError('value not found')         # only reached if no match



