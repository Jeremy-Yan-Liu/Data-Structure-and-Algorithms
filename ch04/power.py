def power(x, n):
    """Compute the value x**n for integer n."""
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

def fast_power(x, n):
    """A more effient implementation for x**n"""
    if n == 0:
        return 1
    else:
        partial = fast_power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result

if __name__ == '__main__':
    import timeit
    print(timeit.timeit('power(5,10)', setup = 'from __main__ import power'))
    print(timeit.timeit('fast_power(5,10)', setup = 'from __main__ import fast_power'))

