def best(W: int, pairs: list) -> tuple:
    return (0, 0)

if __name__ == '__main__':
    print(best(3, [(2, 4), (3, 5)]))
    print(best(3, [(1, 5), (1, 5)]))
    print(best(3, [(1, 2), (1, 5)]))
    print(best(3, [(1, 2), (2, 5)]))
    print(best(58, [(5, 9), (9, 18), (6, 12)]))
    print(best(92, [(8, 9), (9, 10), (10, 12), (5, 6)]))