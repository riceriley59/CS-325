#top-down with memoization
def max_wis_helper(lst, i, memo):
    if i < 0: return (0, [])

    if i in memo: return memo[i]

    # exclude current element
    exclude_sum, exclude_set = max_wis_helper(lst, i-1, memo)

    # include current element
    include_sum, include_set = max_wis_helper(lst, i-2, memo)
    include_sum += lst[i]

    if include_sum > exclude_sum:
        memo[i] = (include_sum, include_set + [lst[i]])
        return memo[i]
    else:
        memo[i] = (exclude_sum, exclude_set)
        return memo[i]

def max_wis(lst):
    memo = {}
    return max_wis_helper(lst, len(lst)-1, memo)


#bottom-up solution
def max_wis2(graph: list) -> tuple:
    mWeight, mSet = 0, []

    return (mWeight, mSet)

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