class SequenceIterator:
    """An iterator for any of Python's sequence types."""

    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence        # keep a reference to the underlying data
        self._k = len(self._seq)    # will increment to 0 on first call to next

    def __next__(self):
        """Return the next element, or else raise StoopIteration error."""
        self._k -= 1                        # advance to next index
        if self._k > -1:
            return(self._seq[self._k])      # return the element
        else:
            raise StopIteration()           # there are no more elements

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self

    def __len__(self):
        return len(self._seq)

class Range:
    """A class that mimic's the built-in range class."""

    def __init__(self, start, stop = None, step = 1):
        """Initialize a Range instance.

        Semantics is similar to built-in range class.
        """
        if step == 0:
            raise ValueError('step cannot be 0.')

        if stop is None:                # special case of range(n)
            start, stop = 0, start      # should be treated as if range(0,n)

        # calculate the effective length once
        self._length = max(0, (stop - start + step - 1) // stop)

        # need knowledge of start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        """Return entry at index k (using standard interpretation if negative)"""
        if k < 0:
            k += len(self)

        if not 0 <= k < self._length:
            raise IndexError('index out of range.')

        return self._start + k * self._step

if __name__ == '__main__':

    seq = SequenceIterator([1,2,3])
    for _ in range(len(seq)):
        print(next(seq))






