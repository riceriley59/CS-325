from bisect import bisect_left

def find(arr: list, x: float, k: int) -> list:
    count = []
    
    i = bisect_left(arr, x)
    i -= 1
    z = (i - 1)

    for y in range(k):
        z_diff = abs(x - arr[z])
        i_diff = abs(x - arr[i])

        if (i_diff < z_diff):
            count.append(arr[i])
            i += 1
        elif (i_diff > z_diff):
            count.append(arr[z])
            z -= 1
        else:
            count.append(arr[z])
            z -= 1

    return count


if __name__ == '__main__':
    print(find([1,2,3,4,4,7], 5.2, 2))
    print(find([1,2,3,4,4,7], 6.5, 3))
    print(find([1,2,3,4,4,6,6], 5, 3))
    print(find([1,2,3,4,4,5,6], 4, 5))