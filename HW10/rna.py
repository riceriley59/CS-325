from collections import defaultdict

def best(rna: str) -> tuple:
    pairs = {'A': 'U', 'U': 'AG', 'C': 'G', 'G': 'CU'}
    n = len(rna)
    best, back = defaultdict(int), defaultdict(lambda: -1)

    def _best(start: int, end: int, best: dict, back: dict) -> tuple:
        if start >= end:
            return 0, -1

        if best[(start, end)] != 0:
            return best[(start, end)], back[(start, end)]

        max_pairs = 0
        max_k = -1

        if rna[start] in pairs[rna[end]]:
            pairs_count, k = _best(start + 1, end - 1, best, back)
            if pairs_count + 1 > max_pairs:
                max_pairs = pairs_count + 1
                max_k = -1

        for k in range(start, end):
            left, left_k = _best(start, k, best, back)
            right, right_k = _best(k + 1, end, best, back)

            if left + right > max_pairs:
                max_pairs = left + right
                max_k = k

        best[(start, end)] = max_pairs
        back[(start, end)] = max_k

        return max_pairs, max_k

    max_pairs, max_k = _best(0, n - 1, best, back)

    # Generate the final structure string using backpointers
    structure_string = ['.'] * n

    def fill_structure(start: int, end: int):
        if start >= end or best[(start, end)] == 0: return

        k = back[(start, end)]
        if k == -1:
            structure_string[start] = '('
            structure_string[end] = ')'
            fill_structure(start + 1, end - 1)
        else:
            fill_structure(start, k)
            fill_structure(k + 1, end)

    fill_structure(0, n - 1)
    structure_string = ''.join(structure_string)

    return max_pairs, structure_string

def total(rna: str) -> int:
    pairs = {'A': 'U', 'U': 'AG', 'C': 'G', 'G': 'CU'}
    n = len(rna)
    count = defaultdict(int)

    def _total(start: int, end: int) -> int:
        if start >= end: return 1

        if count[(start, end)] != 0: return count[(start, end)]

        total_count = _total(start + 1, end)  # Case 1: Ignore current nucleotide

        for k in range(start + 1, end + 1):
            if rna[start] in pairs[rna[k]]:
                total_count += _total(start + 1, k - 1) * _total(k + 1, end)

        count[(start, end)] = total_count

        return total_count

    total_count = _total(0, n - 1)
    return total_count

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
