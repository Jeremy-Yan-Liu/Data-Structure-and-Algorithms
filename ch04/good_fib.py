def good_fibonacci(n):
    """Return the nth Fibonacci number."""

    if n <= 1:
        return (n,0)
    else:
        (a,b) = good_fibonacci(n - 1)
        return (a + b, a)

if __name__ == '__main__':

    print(good_fibonacci(5))
