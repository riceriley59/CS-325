from random import randint

def qselect(k: int, arr: list) -> int:
    if len(arr) == 1:
        return arr[0]

    pivot = arr[randint(0, len(arr) - 1)]

    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]

    pivotIndex = len(left)

    if pivotIndex == (k - 1):
        return pivot
    elif pivotIndex > (k - 1):
        return qselect(k, left)
    else:
        return qselect(k - (len(left) + 1), right)