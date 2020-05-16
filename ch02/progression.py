class Progression:
    """Iterator producing a generic progression.

    Default iterator produces the whole numbers 0,1,2,...
    """
    def __init__(self,start = 0):
        """initialize current to the first value of the progression."""
        self._current = start

    def _advance(self):
        """Update self._current to a new value.

        This should be overriden by a subclass to customize progression.

        By convention, if current is set to None, this designates the end of a finite progression.
        """
        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        if self._current is None:       # our convention to end a progression
            raise StopIteration()
        else:
            answer = self._current      # record current value to return
            self._advance()             # advance to prepare for next time
            return answer               # return the answer

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator"""
        return self

    def print_progression(self,n):
        """Print next n values of the progression"""
        print(' '.join(str(next(self)) for j in range(n)))

class MyFibonacciProgression(Progression):
    """My implementation of Fibonacci Progresssion."""
    def __init__(self, current, _next):
        super().__init__(current)
        self._next = _next
    def _advance(self):
        self._next, self._current = self._next + self._current, self._next

# class ArithmeticProgression(Progression):
#      """Iterator producing an arithmetic progression"""

#     def __init__(self,increment = 1, start = 0):
#         """Create a new arithmetic progrerssion
#         increment the fixed constant to add to each term (default 1)
#         start     the first term of the progression (default 0)
#         """
#         super().__init__(start)
#         self._increment = increment

#     def _advance(self):
#         """Update current value by adding the fixed increment"""
#         self._current += self._increment

class GeometricProgression(Progression):   # inherit from Progression
    """Iterator producing a geometric progression"""

    def __init__(self, base = 2, start = 1):
        """Create a new geometric progrerssion
        base      the fixed constant to multiply to each term (default 2)
        start     the first term of the progression (default 0)
        """
        super().__init__(start)
        self._base = base

    def _advance(self):                     # override inherited version
        """Update current value by multiplying the fixed base"""
        self._current *= self._base

class FibonacciProgression(Progression):   # inherit from Progression
    """Iterator producing a fibonacci progression"""

    def __init__(self, first = 0, second = 1):
        """Create a new fibonacci progrerssion
        first     the first term of the progression (default 0)
        second    the second term of the progression (default 1)
        """
        super().__init__(first)             # start progression at first
        self._prev = second - first         # fictitious value preceding the first

    def _advance(self):                     # override inherited version
        """Update current value by taking sum of previous two."""
        self._prev, self._current = self._current , self._current + self._prev


if __name__ == '__main__':

    # print('default progression:')
    # progression().print_progression(10)

    # print('arithmetic progression with increment 5:')
    # arithmeticprogression(5).print_progression(10)


    # print('arithmetic progression with increment 5 and 2:')
    # arithmeticprogression(5,2).print_progression(10)


    # print('geometric progressionn with default base:')
    # geometricprogression().print_progression(10)


    # print('geometric progression with base 3:')
    # geometricprogression(3).print_progression(10)


    # print('fibonacci progression with default start values:')
    # fibonacciprogression().print_progression(10)


    print('fibonacci progression with start values 4 and 6:')
    FibonacciProgression(2, 2).print_progression(10)

    print('fibonacci progression with start values 2 and 2:')
    MyFibonacciProgression(2, 2).print_progression(10)

