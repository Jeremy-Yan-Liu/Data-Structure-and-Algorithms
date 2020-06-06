def quick_sort(S):
    """Sort the elements of queue S using the quick-sort algorithm."""
    n = len(S)
    if n < 2:
        return                              # list is already sorted
    # divide
    p = S.first()                           # using first as arbitrary pivot
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()
    while not S.is_empty():                 # divide S into L, E, and G
        if S.first() < p:
            L.enqueue(S.dequeue())
        elif p < S.first():
            G.enqueue(S.dequeue())
        else:
            E.enqueue(S.dequeue())
    # conquer (with recursion)
    quick_sort(L)                           # sort elements less than p
    quick_sort(G)                           # sort elements greater than p
    # concatenate results
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())

def inplace_quick_sort(S, a, b):
    """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm."""
    if a >= b: return                       # range is trivially sorted
    pivot = S[b]                            # last element of range is pivot
    left = a                                # will scan rightward
    right = b - 1                           # will scan leftward
    while left < = right:
        # scan until reaching value equal or larger than pivot (or right marker)
        while left <= right and S[left] < pivot:
            left += 1
        # scan until reaching value qual or smaller than pivot (or left marker)
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:                   # scans did not strictly cross
            S[left], S[right] = S[right], S[left]       # swap values
            left, right = left + 1, right - 1           # shrink range
    # put pivot into its final place (currently marked by left index)
    S[left], S[b] = S[b], S[left]
    # mark recursive calls
    inplace_quick_sort(S, a, left - 1)
    inplace_quick_sort(S, left + 1, b)
