from heapdict import heapdict
from collections import defaultdict

def shortest(n, edges):
    # Create an adjacency list to represent the graph
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # Initialize the distance dictionary
    distances = defaultdict(lambda : float('inf'))
    distances[0] = 0

    # Initialize the priority queue
    pq = heapdict()
    pq[0] = 0

    # Initialize the parent dictionary
    parent = defaultdict(lambda : None)

    while pq:
        u, dist_u = pq.popitem()

        if u == n - 1: break

        if dist_u > distances[u]: continue

        for v, weight in graph[u]:
            new_dist = dist_u + weight
            if new_dist < distances[v]:
                distances[v] = new_dist
                parent[v] = u
                pq[v] = new_dist

    if n - 1 not in parent: return None

    # Reconstruct the shortest path
    path = []
    node = n - 1
    while node is not None:
        path.append(node)
        node = parent[node]

    return distances[n - 1], path[::-1]


if __name__ == '__main__':
    print(shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
    print(shortest(5, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
    print(shortest(4, [(0,1,1), (2,3,1)]))