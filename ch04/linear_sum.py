def linear_sum(S, n):
    """Return the sum of the first n numbers of sequence S."""
    if n == 0:
        return 0
    else:
        return linear_sum(S,n-1) + S[n-1]

if __name__ == '__main__':

    S = [1,2,4]
    print(linear_sum(S,2))
    print(linear_sum(S,1))

