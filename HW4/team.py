from heapq import heapify, heappop, heappush, heapreplace

def select(*a: list) -> list:
    output = []

    heap = [(x[0], i, 0) for i, x in enumerate(a)]
    heapify(heap)

    while heap:
        x, i, j = heappop(heap)
        output.append(x)
        if j < len(a[i]) - 1: heappush(heap, (a[i][j + 1], i, j + 1))

    return output[:len(a[0])]

if __name__ == '__main__':
    print(select([1, 5, 7, 9], [2, 4, 8, 10], [0, 3, 6, 9]))
    print(select([16, 18], [0, 10], [5, 7], [2, 9], [11, 19], [8, 17], [6, 13], [1, 11], [14, 16], [1, 4]))