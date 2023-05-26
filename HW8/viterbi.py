from collections import defaultdict

def topsort(n: int, edges: list) -> list:
    adj_list, deg, q, solution = defaultdict(list), defaultdict(int), [], []
    for x, y in edges: 
        adj_list[x].append(y)
        deg[y] += 1

    for node in range(n):
        if deg[node] == 0: q.append(node)

    while len(q) > 0:
        node = q.pop()
        solution.append(node)

        for neighbor in adj_list[node]:
            deg[neighbor] -= 1
            if deg[neighbor] == 0: q.append(neighbor)


    if len(solution) == n: return solution
    else: return None

def longest(n: int, edges: list) -> tuple:
    top, best, back = topsort(n, edges), defaultdict(int), defaultdict(int)

    adj_list = defaultdict(list)

    for x, y in edges: adj_list[x].append(y)

    for v in top:
        for u in adj_list[v]:
            new = best[v] + 1

            if new > best[u]:
                best[u] = new
                back[u] = v

    return (best[n - 1], back)
            

if __name__ == '__main__':
    print(longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
    print(longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
    print(longest(8, [(0,1), (0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7), (6,7)]))