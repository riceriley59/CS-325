from collections import defaultdict

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

    def fill_structure(start: int, end: int, structure: list):
        if start >= end or best[(start, end)] == 0: return

        k = back[(start, end)]
        if k == -1:
            structure[start] = '('
            structure[end] = ')'
            fill_structure(start + 1, end - 1, structure)
        else:
            fill_structure(start, k, structure)
            fill_structure(k + 1, end, structure)

    fill_structure(0, n - 1, structure_string)

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
    return None

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
