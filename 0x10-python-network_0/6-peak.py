#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
    list_of_integers (list): List of unsorted integers.

    Returns:
    int: A peak value from the list.

    Complexity:
    The complexity of this algorithm is O(log(n)), as it
    divides the list in half with each iteration.
    """
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # If mid element is greater than its right neighbor, move left.
            low = mid + 1
        else:
            # Otherwise, move right.
            high = mid

    return list_of_integers[low]
