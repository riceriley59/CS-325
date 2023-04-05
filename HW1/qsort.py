def sorted(t: list) -> list:
    sortlist = []

    if t:
        left = t[0]
        sorted(left)

        sortlist.append(t[1])

        right = t[2]
        sorted(right)

        return sortlist
    
    return None


def search(t: list, x: int) -> bool:
    return True

def insert(t: list, x: int) -> None:
    return


tree = [[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]

print(sorted(tree))