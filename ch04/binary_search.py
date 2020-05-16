def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of a Python list."""

    if low > high:
        return False                        # interval is empty, return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)

if __name__ == '__main__':

    data = [1,2,5,19,20,66]
    print(binary_search(data, 6, 0, len(data)))
    print(binary_search(data, 5, 0, len(data)))

