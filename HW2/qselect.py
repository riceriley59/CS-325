import random
import math

#returns kth lowest number in given array using quickselect
def qselect(k: int, arr: list) -> int:
    value = _kthSmallest(k, arr, 0, len(arr) - 1)
    if value != math.inf: return value
    else: return ValueError


def _kthSmallest(k: int, arr: list, start: int, end: int):
    if(k > 0 and k <= (end - start) + 1):
        narray = arr[start:end]
        pivot = arr[random.randint(start, end)]

        left = [x for x in narray if x < pivot]
        right = [x for x in narray if x > pivot]

        pivotIndex = start + len(left)

        if(pivotIndex == k): return arr[pivotIndex]
        if(pivotIndex < k): return _kthSmallest(k, arr, pivotIndex, end)
        else: return _kthSmallest(k, arr, start, pivotIndex)

    return math.inf

        

if __name__ == '__main__':
    print(qselect(2, [3, 10, 4, 7, 19]))
    print(qselect(4, [11, 2, 8, 3]))