def _max_depth(tree: list) -> int:
    if not tree: return (0, 0)

    left, root, right = tree

    lpath, lheight = _max_depth(left)
    rpath, rheight = _max_depth(right) 

    return (max(lheight + rheight, lpath, rpath), max(lheight, rheight) + 1) 

longest = lambda tree: _max_depth(tree)[0]

if __name__ == "__main__":
    print(longest([[], 1, []]))
    print(longest([[[], 1, []], 2, [[], 3, []]]))
    print(longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]))