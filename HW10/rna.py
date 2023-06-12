from collections import defaultdict
import heapq

def fill_structure(start: int, end: int, structure: list, back: dict, best: dict):
    if start >= end or best[(start, end)] == 0: return

    k = back[(start, end)]
    if k == -1:
        structure[start] = '('
        structure[end] = ')'
        fill_structure(start + 1, end - 1, structure, back, best)
    else:
        fill_structure(start, k, structure, back, best)
        fill_structure(k + 1, end, structure, back, best)

def best(rna: str) -> tuple:
    pairs = {'A': 'U', 'U': 'AG', 'C': 'G', 'G': 'CU'}
    n = len(rna)
    best = defaultdict(int); back = defaultdict(lambda: -1)

    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            max_pairs = best[(i, j)]

            if rna[i] in pairs[rna[j]]: 
                max_pairs = max(max_pairs, best[(i + 1, j - 1)] + 1)

            for k in range(i, j):
                pairs_count = best[(i, k)] + best[(k + 1, j)]
                if pairs_count > max_pairs:
                    max_pairs = pairs_count
                    back[(i, j)] = k

            best[(i, j)] = max_pairs

    # Generate the final structure string using backpointers
    structure_string = ['.'] * n

    fill_structure(0, n - 1, structure_string, back, best)

    return best[(0, n - 1)], ''.join(structure_string)

def total(rna: str) -> int:
    pairs = {'A': 'U', 'U': 'AG', 'C': 'G', 'G': 'CU'}
    n = len(rna)
    count = defaultdict(int)

    def _total(start: int, end: int) -> int:
        if start >= end: return 1

        if count[(start, end)] != 0: return count[(start, end)]

        total_count = _total(start + 1, end)

        for k in range(start + 1, end + 1):
            if rna[start] in pairs[rna[k]]:
                total_count += _total(start + 1, k - 1) * _total(k + 1, end)

        count[(start, end)] = total_count

        return total_count
    
    return _total(0, n - 1)

def kbest(rna: str, k: int) -> list:
    pairs, pq = {'A': 'U', 'U': 'AG', 'C': 'G', 'G': 'CU'}, []
    best, back, n = defaultdict(int), defaultdict(lambda: -1), len(rna)

    def find_kbest(start: int, end: int, k: int):
        if start >= end:
            return

        if k == 0:
            return

        max_pairs = best[(start, end)]

        if max_pairs == k:
            structure = ['.'] * n
            fill_structure(start, end, structure, back, best)
            structure_string = ''.join(structure)
            heapq.heappush(pq, (-max_pairs, structure_string))

        for k in range(start, end):
            pairs_count = best[(start, k)] + best[(k + 1, end)]

            if pairs_count >= k:
                find_kbest(start, k, k - best[(k + 1, end)])
                find_kbest(k + 1, end, k - best[(start, k)])

    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            max_pairs = best[(i, j)]

            if rna[i] in pairs[rna[j]]:
                max_pairs = max(max_pairs, best[(i + 1, j - 1)] + 1)

            for k in range(i, j):
                pairs_count = best[(i, k)] + best[(k + 1, j)]
                if pairs_count > max_pairs:
                    max_pairs = pairs_count
                    back[(i, j)] = k

            best[(i, j)] = max_pairs

    find_kbest(0, n - 1, k)
    kbest_structures = heapq.nsmallest(min(k, len(pq)), pq)

    return [(-pairs, structure) for pairs, structure in kbest_structures]

if __name__ == '__main__': 
    # Test cases
    test_cases = [
        "ACAGU",
        "AC",
        "GUAC",
        "GCACG",
        "CCGG",
        "CCCGGG",
        "UUCAGGA",
        "AUAACCUA",
        "UUGGACUUG",
        "UUUGGCACUA",
        "GAUGCCGUGUAGUCCAAAGACUUC",
        "AGGCAUCAAACCCUGCAUGGGAGCG"
    ]

    for s in test_cases:
        print(best(s))
        print(total(s))
        print(kbest(s, 10))
