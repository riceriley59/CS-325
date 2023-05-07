#top-down solution with memoization
def _bst_helper(n: int, best: dict) -> int:
    if n in best: return best[n]
    
    num = 0

    for i in range(1, n + 1): num += _bst_helper(i - 1, best) * _bst_helper(n - i, best)

    best[n] = num; return best[n]

def bsts(n: int) -> int:
    best = {0: 1}

    return _bst_helper(n, best)

#bottom-up solution
def bsts2(n: int) -> int:
    best = dict.fromkeys(range(n + 1), 0)
    best[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            best[i] += best[j] * best[i - j - 1]

    return best[n]

if __name__ == '__main__':
    print("Top-down Solution with memoization:")
    print(bsts(2))
    print(bsts(3))
    print(bsts(5))

    print("\nBottom-up solution")
    print(bsts2(2))
    print(bsts2(3))
    print(bsts2(5))