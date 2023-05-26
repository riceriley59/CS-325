from collections import defaultdict

def longest(n: int, edges: list) -> tuple:
    adj_list, deg, q, solution = defaultdict(list), defaultdict(int), [], []
    for x, y in edges: 
        adj_list[x].append(y)
        deg[y] += 1

    # Perform topological sort
    for node in range(n):
        if deg[node] == 0: 
            q.append(node)

    while len(q) > 0:
        node = q.pop()
        solution.append(node)

        for neighbor in adj_list[node]:
            deg[neighbor] -= 1
            if deg[neighbor] == 0: 
                q.append(neighbor)

    # Perform Viterbi algorithm
    longest_paths = defaultdict(int)  # Initialize longest paths
    path = defaultdict(lambda: None)  # Initialize path

    for node in solution:
        for neighbor in adj_list[node]:
            if longest_paths[node] + 1 > longest_paths[neighbor]:
                longest_paths[neighbor] = longest_paths[node] + 1
                path[neighbor] = node

    max_length = max(longest_paths)
    max_index = longest_paths[max_length]

    # Construct the path
    longest_path = [max_index]
    while path[max_index] is not None:
        max_index = path[max_index]
        longest_path.append(max_index)
    longest_path.reverse()

    return max_length, longest_path

if __name__ == '__main__':
    print(longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
    print(longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
    print(longest(8, [(0,1), (0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7), (6,7)]))
    print(longest(8, [(0,1), (0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7), (6,7)]))