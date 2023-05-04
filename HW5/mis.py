#top-down with memoization
def max_wis(graph: list) -> tuple:
    mWeight, mSet = 0, []

    

    return (mWeight, mSet)

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
    
    print("\nBottom-up solution")
    print(max_wis2([7,8,5]))
    print(max_wis2([-1,8,10]))
    print(max_wis2([]))
    print(max_wis2([-5, -1, -4]))