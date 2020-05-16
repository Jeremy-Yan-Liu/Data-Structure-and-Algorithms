def binary_sum(S, start, stop):
    """Return the sum of the numbers in implicit slice S[start, stop]"""
    if start >= stop:               # zero elements in slice
        return 0
    elif start == stop - 1:         # one element in slice
        return S[start]
    else:                           # two or more elements in slice
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)

if __name__ == '__main__':

    S = list(range(10))
    print(S)
    print(binary_sum(S, 2, 7))
    print(binary_sum(S, 0, len(S)))

