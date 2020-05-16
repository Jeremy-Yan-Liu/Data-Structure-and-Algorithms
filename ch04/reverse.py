def reverse(S, start, stop):
    """Reverse elements in implicit slice S[start, stop]"""
    if start < stop - 1:                                    # if at least 2 elements
        S[start], S[stop - 1] = S[stop - 1], S[start]       # swap first and last
        # print(S, start, stop)
        reverse(S, start + 1, stop - 1)                     # recur on rest

if __name__ == '__main__':
    S = list(range(5))
    print(S)
    reverse(S, 0,len(S))
    print(S)
