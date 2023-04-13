def num_inversions(arr: list) -> int:
    inversions = 0

    if(len(arr) > 1):
        middle = len(arr) // 2

        left = arr[:middle]
        right = arr[middle:]

        inversions += num_inversions(left)
        inversions += num_inversions(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                inversions += (middle - i)
            
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return inversions
