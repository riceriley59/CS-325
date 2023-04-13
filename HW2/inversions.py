#number of num_inversions
def _num_inversions(arr: list) -> int:
    if arr == []: return ([], 0)
    
    pivot = arr[0]

    left, right, num = [], [], 0

    for x in arr[1:]:
        if x > pivot: right.append(x)
        else: 
            left.append(x)
            num += len(right) + 1
    
    leftA, lnum = _num_inversions(left)
    rightA, rnum = _num_inversions(right)

    return (leftA + [pivot] + rightA, lnum + rnum + num)

num_inversions = lambda arr: _num_inversions(arr)[1]

if __name__ == "__main__":
    print(num_inversions([5, 4, 3, 2, 1]))