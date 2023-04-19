from bisect import bisect_left

def find(arr: list, x: float, k: int) -> list:
    i = bisect_left(arr, x)
    
    left = (i - 1)
    right = i
    
    while k > 0 and (left >= 0 or right <= len(arr)):
        if left < 0:
            right += 1
        elif right == len(arr):
            left -= 1
        elif abs(arr[left] - x) <= abs(arr[right] - x):
            left -= 1
        else:
            right += 1
        k -= 1
    
    return arr[left+1:right]