def kmergesort(A, k):
    n = len(A)
    if n <= 1:
        return A
    sublists = [kmergesort(A[i:i+n//k], k) for i in range(0, n, n//k)]
    result = []
    while any(sublists):
        min_vals = [lst[0] for lst in sublists if lst]
        min_val = min(min_vals)
        min_idxs = [i for i, lst in enumerate(sublists) if lst and lst[0] == min_val]
        for idx in min_idxs:
            sublists[idx] = sublists[idx][1:]
        result.append(min_val)
    return result

if __name__ == "__main__":
    print(kmergesort([4,1,5,2,6,3,7,0], 3))