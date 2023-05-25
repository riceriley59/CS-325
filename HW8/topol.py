from collections import defaultdict

def order(n: int, edges: list) -> list:
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

if __name__ == '__main__':
    print(order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
    print(order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
    print(order(4, [(0,1), (1,2), (2,1), (2,3)]))
    print(order(5, [(0,1), (1,2), (2,3), (3,4)]))
    print(order(5, []))
    print(order(3, [(1,2), (2,1)]))
    print(order(1, [(0,0)]))