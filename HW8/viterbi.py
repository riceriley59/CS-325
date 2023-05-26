from collections import defaultdict

def longest(n: int, edges: list) -> tuple:
    if not edges:
        return 0, []

    adj_list, indegree, q, solution = defaultdict(list), defaultdict(int), [], []
    for x, y in edges:
        adj_list[x].append(y)
        indegree[y] += 1

    for node in range(n):
        if indegree[node] == 0:
            q.append(node)

    while q:
        node = q.pop()
        solution.append(node)

        for neighbor in adj_list[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    best, back = defaultdict(int), defaultdict(lambda: None)

    for node in solution:
        for neighbor in adj_list[node]:
            if best[node] + 1 > best[neighbor]:
                best[neighbor] = best[node] + 1
                back[neighbor] = node

    path = []
    node = best[n - 1]
    while node is not None:
        path.append(node)
        node = back[node]
        
    path.reverse(); return (best[n - 1], path)


if __name__ == '__main__':
    print(longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
    print(longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
    print(longest(8, [(0,1), (0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7), (6,7)]))
    print(longest(8, [(0,1), (0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7), (6,7)]))