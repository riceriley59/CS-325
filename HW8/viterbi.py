from collections import defaultdict

def longest(n: int, edges: list) -> list:
    adj_list, output, best, back = defaultdict(list), [], defaultdict(int), defaultdict(lambda : -1)
    for x, y in edges: adj_list[x].append(y)

    cycle, visited = set(), set()
    def top(curr: int):
        if curr in cycle: return False
        if curr in visited: return True

        cycle.add(curr)
        for u in adj_list[curr]:
            if not top(u): return False

            new = best[u] + 1
            if new > best[curr]:
                best[curr] = new
                back[curr] = u
        
        cycle.remove(curr); visited.add(curr)
        output.append(curr)
        return True

    for c in range(n):
        if not top(c): return None

    path, index = [], 0
    while index <= n - 1:
        if back[index] == -1:
            path.append(index)
            break
        path.append(index)
        index = back[index]

    return (best[0], path)    

if __name__ == '__main__':
    print(longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
    print(longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
    print(longest(8, [(0,1), (0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7), (6,7)]))
    print(longest(8, [(0,1), (0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7), (6,7)]))