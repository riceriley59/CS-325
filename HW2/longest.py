def _depth(tree: list) -> int:
    if not tree: return 0
    
    left, center, right = tree

    return max((longest(left) + 1), (longest(right) + 1))
    

def longest(tree: list) -> int:
    if not tree: return 0

    left, center, right = tree

    return _depth(left) + _depth(right) + 1

if __name__ == "__main__":
    print(longest([[], 1, []]))
    print(longest([[[], 1, []], 2, [[], 3, []]]))
    print(longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]))