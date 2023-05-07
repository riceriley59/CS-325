#top-down with memoizaton
def _num_no_helper(n: int, best: dict) -> int:
    if n in best: return best[n]

    best[n] = _num_no_helper(n - 1, best) + _num_no_helper(n - 2, best)

    return best[n]

def num_no(n: int) -> int:
    best = {0: 1, 1: 2}; return _num_no_helper(n, best)

#top-down with memoization
def _num_yes_helper(n: int, best: dict) -> int:
    if n in best: return best[n]

    best[n] = _num_yes_helper(n - 1, best) + _num_no_helper(n - 2, best)

    return best[n]

def num_yes(n: int) -> int:
    best = {0: 1, 1: 1}; return _num_yes_helper(n, best)

if __name__ == '__main__':
    print(num_no(3))
    print(num_yes(3))