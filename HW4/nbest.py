import heapq
from random import randint

def nbesta(a: list, b: list) -> list:
    nbest = [(x, y) for x in a for y in b]
    nbest.sort(key=lambda p: (p[0] + p[1], p[1]))
    return nbest[:len(a)]

def qselect(k: int, a: list) -> int:
    index = randint(0, len(a)-1) # randomized pivot position
    a[0], a[index] = a[index] , a[0] # swap pivot with a[0]
    pivot = a[0]
        
    left = [x for x in a if x < pivot]
    right = [x for x in a[1:] if x >= pivot]

    left_size = len(left) + 1 # including pivot
    if k == left_size: return pivot
    return qselect(k, left) if k < left_size else qselect(k - left_size, right)

def nbestb(a: list, b: list) -> list:
    nbest = [(x, y) for x in a for y in b]
    for i in range(len(a) - 1): nbest.insert(0, qselect(len(a) - i, nbest))
    return nbest[:len(a)]

def nbestc(A, B):
    n = len(A)
    res = []
    heap = [(A[0] + B[j], 0, j) for j in range(n)]
    heapq.heapify(heap)
    visited = set((0, j) for j in range(n))
    while len(res) < n:
        s, i, j = heapq.heappop(heap)
        res.append((A[i], B[j]))
        if i+1 < n and (i+1, j) not in visited:
            heapq.heappush(heap, (A[i+1] + B[j], i+1, j))
            visited.add((i+1, j))
        if j+1 < n and (i, j+1) not in visited:
            heapq.heappush(heap, (A[i] + B[j+1], i, j+1))
            visited.add((i, j+1))
    return res


if __name__ == '__main__':
    a, b = [4, 1, 5, 3], [2, 6, 3, 4]
    print(nbesta(a, b))
    print(nbestb(a, b))
    print(nbestc(a, b))