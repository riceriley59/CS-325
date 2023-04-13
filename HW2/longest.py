def longest(tree: list) -> int:
    if not tree: return 0

    left, center, right = tree

    

if __name__ == "__main__":
    print(longest([[], 1, []]))
    print(longest([[[], 1, []], 2, [[], 3, []]]))
    print(longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]))