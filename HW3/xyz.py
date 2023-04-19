def find(arr: list) -> list:
    n = len(arr)

    arr.sort()

    output = []

    for i in range(n):
        for j in range(i+1, n):
            z = arr[i] + arr[j]
            if z in arr[j+1:]:
                output.append((arr[i], arr[j], z))

    return output


if __name__ == "__main__":
    print(find([1, 4, 2, 3, 5]))