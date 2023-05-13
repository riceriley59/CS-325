def best(W: int, triples: list) -> tuple:
    return (0, 0)

if __name__ == '__main__':
    print(best(3, [(2, 4, 2), (3, 5, 3)]))
    print(best(3, [(1, 5, 2), (1, 5, 3)]))
    print(best(3, [(1, 5, 1), (1, 5, 3)]))
    print(best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))
    print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))