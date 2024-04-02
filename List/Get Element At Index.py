

#Get Element At Index

def getElementAtIndex(arr, n, i):
    """
    Returns the element at index i in the array arr.
    If the index is out of bounds, returns -1.
    """
    if i >= 0 and i < n:
        return arr[i]
    else:
        return -1

