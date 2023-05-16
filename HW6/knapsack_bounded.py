def backpoint(back: dict, W: int, items: int) -> list:
    result = [0] * len(items)

    w, i = W, len(items) - 1

    while i >= 0 and w > 0:
        j = back[(w, i)]
        result[i] = j
        w -= j * items[i][0]
        i -= 1

    return result

def best(W: int, items: list) -> tuple:
    bestdict, back = {}, {}

    def dp(w: int, i: int) -> int:
        if (w, i) in bestdict: return bestdict[(w, i)]

        if i < 0 or w <= 0: return 0

        weight, value, count = items[i]

        bestdict[(w, i)] = 0

        for j in range(count + 1):
            if j * weight > w: break

            val = dp(w - j * weight, i - 1) + j * value

            if val > bestdict[(w, i)]:
                bestdict[(w, i)] = val
                back[(w, i)] = j

        return bestdict[(w, i)]

    return (dp(W, len(items) - 1), backpoint(back, W, items))

if __name__ == '__main__':
    print(best(3, [(2, 4, 2), (3, 5, 3)]))
    print(best(3, [(1, 5, 2), (1, 5, 3)]))
    print(best(3, [(1, 5, 1), (1, 5, 3)]))
    print(best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]))
    print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]))