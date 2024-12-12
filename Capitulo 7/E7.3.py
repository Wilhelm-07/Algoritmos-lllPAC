def quickselect(arr, left, right, k):
    """
    Finds the k-th smallest element in an array.

    Args:
        arr: The input array.
        left: The left index of the subarray.
        right: The right index of the subarray.
        k: The index of the desired element (0-based).

    Returns:
        The k-th smallest element.
    """
    if left == right:
        return arr[left]

    pivot_index = partition(arr, left, right)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, left, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, right, k)

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

def median(arr):
    """
    Finds the median of an array.

    Args:
        arr: The input array.

    Returns:
        The median of the array.
    """
    n = len(arr)
    return quickselect(arr, 0, n - 1, n // 2)