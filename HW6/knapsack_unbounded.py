def best(W: int, items: list) -> tuple:
    best_values = [0] * (W + 1)
    last_item = [-1] * (W + 1)
    
    for weight in range(1, W + 1):
        best_value = 0
        for i in range(len(items)):
            if items[i][0] <= weight:
                value = best_values[weight - items[i][0]] + items[i][1]
                if value > best_value:
                    best_value = value
                    last_item[weight] = i

        best_values[weight] = best_value

    picks = [0] * len(items)
    weight = W
    while weight > 0 and last_item[weight] != -1:
        picks[last_item[weight]] += 1
        weight -= items[last_item[weight]][0]

    return (best_values[W], picks)

if __name__ == '__main__':
    print(best(3, [(2, 4), (3, 5)]))
    print(best(3, [(1, 5), (1, 5)]))
    print(best(3, [(1, 2), (1, 5)]))
    print(best(3, [(1, 2), (2, 5)]))
    print(best(58, [(5, 9), (9, 18), (6, 12)]))
    print(best(92, [(8, 9), (9, 10), (10, 12), (5, 6)]))