import heapq

def ksmallest(k: int, stream: list) -> list:
    heap = []

    for i, x in enumerate(stream):
        if i < k:
            heap.append(-x)
            if i == k - 1: heapq.heapify(heap)
        else:
            if heap and -x > heap[0]:
                heapq.heapreplace(heap, -x)

    return sorted([-x for x in heap])
    

if __name__ == '__main__':
    print(ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]))
    print(ksmallest(3, range(1000000, 0, -1)))