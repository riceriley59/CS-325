#number of inversions
def inversions(arr: list) -> int:
    if arr == []: return ([], 0)
    
    pivot = arr[0]

    left, right, num = [], [], 0

    for x in arr[1:]:
        if x > pivot: right.append(x)
        else: 
            left.append(x)
            num += len(right) + 1
    
    leftA, lnum = inversions(left)
    rightA, rnum = inversions(right)

    return (leftA + [pivot] + rightA, lnum + rnum + num)