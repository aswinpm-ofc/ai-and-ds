def binary_search(arr, target):
    """
    Perform binary search on a sorted array.

    Args:
    arr (list): A sorted list of elements.
    target: The element to search for.

    Returns:
    int: The index of the target if found, otherwise -1.
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid  # Target found
        elif mid_val < target:
            low = mid + 1  # Search the right half
        else:
            high = mid - 1  # Search the left half

    return -1  # Target not found

