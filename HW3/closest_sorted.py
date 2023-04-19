from bisect import bisect_left

def find(A, x, k):
    i = bisect_left(A, x)
    
    left = (i - 1)
    right = i
    
    while k > 0 and (left >= 0 or right <= len(A)):
        if left < 0:
            right += 1
        elif right == len(A):
            left -= 1
        elif abs(A[left] - x) <= abs(A[right] - x):
            left -= 1
        else:
            right += 1
        k -= 1
    
    return A[left+1:right]