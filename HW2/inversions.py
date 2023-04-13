#number of num_inversions
def num_inversions(arr: list) -> int:
    if arr == []: return ([], 0)
    
    pivot = arr[0]

    left, right, num = [], [], 0

    for x in arr[1:]:
        if x > pivot: right.append(x)
        else: 
            left.append(x)
            num += len(right) + 1
    
    leftA, lnum = num_inversions(left)
    rightA, rnum = num_inversions(right)

    return (leftA + [pivot] + rightA, lnum + rnum + num)

if __name__ == "__main__":
    print(num_inversions([5, 4, 3, 2, 1]))