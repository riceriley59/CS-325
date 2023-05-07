#top-down with memoization
def max_wis_helper(graph: list, i: int, best: dict) -> tuple:
    if i in best: return best[i][0]

    # exclude current element
    exclude_sum = max_wis_helper(graph, i - 1, best)

    # include current element
    include_sum = max_wis_helper(graph, i - 2, best)
    include_sum += graph[i]

    if include_sum > exclude_sum: best[i] = (include_sum, True)
    else: best[i] = (exclude_sum, False)

    return best[i][0]

def max_wis(graph: list) -> tuple:
    mbest, result = {-2: (0, False), -1: (0, False)}, []

    msum, ilast = max_wis_helper(graph, len(graph) - 1, mbest), len(graph) - 1

    while ilast >= 0:
        if mbest[ilast][1] == True:
            result.append(graph[ilast])
            ilast -= 2
        else:
            ilast -= 1

    result.reverse()

    return (msum, result)

#bottom-up solution
def max_wis2(graph: list) -> tuple:
    mbest, result, ilast = {-2: (0, False), -1: (0, False)}, [], len(graph) - 1

    for i in range(0, len(graph)):
        exclude_sum = mbest[i - 1][0]
        include_sum = mbest[i - 2][0]
        include_sum += graph[i]

        if include_sum > exclude_sum: mbest[i] = (include_sum, True)
        else: mbest[i] = (exclude_sum, False)

    while ilast >= 0:
        if mbest[ilast][1] == True:
            result.append(graph[ilast])
            ilast -= 2
        else:
            ilast -= 1

    result.reverse()
    
    return (mbest[len(graph) - 1][0], result)

if __name__ == '__main__':
    print("Top-down solution with memoization:")
    print(max_wis([7,8,5]))
    print(max_wis([-1,8,10]))
    print(max_wis([]))
    print(max_wis([-5, -1, -4]))
    
    print("\nBottom-up solution:")
    print(max_wis2([7,8,5]))
    print(max_wis2([-1,8,10]))
    print(max_wis2([]))
    print(max_wis2([-5, -1, -4]))