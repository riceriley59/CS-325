from bisect import bisect_left

def find(arr: list, x: float, k: int) -> list:
    i = bisect_left(arr, x)
    
    left = (i - 1)
    right = i
    
    for y in range(k):
        if left < 0:
            right += 1
        elif right == len(arr):
            left -= 1
        elif abs(arr[left] - x) <= abs(arr[right] - x):
            left -= 1
        else:
            right += 1
    
    return arr[left+1:right]

if __name__ == '__main__':
    print(find([1,2,3,4,4,7], 5.2, 2))
    print(find([1,2,3,4,4,7], 6.5, 3))
    print(find([1,2,3,4,4,6,6], 5, 3))
    print(find([1,2,3,4,4,5,6], 4, 5))