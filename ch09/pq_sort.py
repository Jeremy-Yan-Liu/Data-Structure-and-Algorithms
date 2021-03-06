def pq_sort(C):
    """Sort a collection of elements sttored in a positional list."""
    n = len(C)
    P = PriorityQueue()
    for j in range(n):
        element = C.delete(C.first())
        P.add(element, element)         # use element as key and value
    for j in range(n):
        (k,v) = P.remove_min()
        C.add_last(v)                   # store smallest remaining element in C
