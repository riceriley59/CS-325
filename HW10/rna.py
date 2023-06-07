from collections import defaultdict

pairs = {
    'A': {'U'},
    'G': {'G'},
    'C': {'G'},
    'U': {'A', 'G'}
}

def best(rna: str) -> tuple:
    n = len(rna)
    best, back = defaultdict(int), defaultdict(int)

    def _best(start: int, end: int, best: dict, back: dict) -> tuple:
        if start >= end: return 0, ''

        if best[(start, end)] != 0: return best[(start, end)], back[(start, end)]

        max_pairs = 0; max_structure = ''

        if rna[start] in pairs[rna[end]]:
            pairs_count, structure = _best(start + 1, end - 1, best, back)
            max_pairs = pairs_count + 1
            max_structure = f'({structure})'

        for k in range(start, end):
            left, left_str = _best(start, k, best, back)
            right, right_str = _best(k + 1, end, best, back)

            if left + right > max_pairs:
                max_pairs = left + right
                max_structure = left_str + right_str

        best[(start, end)] = max_pairs
        back[(start, end)] = max_structure

        return max_pairs, max_structure

    max_pairs, max_structure = _best(0, n - 1, best, back)
    return max_pairs, max_structure

def total(rna: str) -> int:
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

def kbest(rna: str, k: int) -> list[tuple]:
    results = []

    def _kbest(start: int, end: int, k: int, structure: str):
        if start >= end or k <= 0:
            pairs, _ = best(structure)
            results.append((pairs, structure))
            return

        if rna[start] in pairs[rna[end]]:
            _kbest(start + 1, end - 1, k - 1, f'({structure})')

        for i in range(start, end):
            left_pairs, _ = best(structure[:i - start + 1])
            right_pairs, _ = best(structure[i - start + 1:])

            if left_pairs + right_pairs >= k:
                _kbest(start, i, k, structure[:i - start + 1])
                _kbest(i + 1, end, k, structure[i - start + 1:])

    _kbest(0, len(rna), k, '')
    results.sort(reverse=True)
    return results[:k]

if __name__ == '__main__': 
    # Testing the provided examples
    print(best("UUCAGGA"))  # (3, '(((.)))')
    print(best("GUUAGAGUCU"))  # (4, '(.()((.)))')
    print(best("AUAACCUUAUAGGGCUCUG"))  # (8, '.(((..)()()((()))))')
    print(best("AACCGCUGUGUCAAGCCCAUCCUGCCUUGUU"))  # (11, '(((.(..(.((.)((...().))()))))))')
    print(best("GAUGCCGUGUAGUCCAAAGACUUCACCGUUGG"))  # (14, '.()()(()(()())(((.((.)(.))()))))')
    print(best("CAUCGGGGUCUGAGAUGGCCAUGAAGGGCACGUACUGUUU"))  # (18, '(()())(((((.)))()(((())(.(.().()()))))))')
    print(best("ACGGCCAGUAAAGGUCAUAUACGCGGAAUGACAGGUCUAUCUAC"))  # (19, '.()(((.)(..))(((.()()(())))(((.)((())))))())')
    print(best("AGGCAUCAAACCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA"))  # (20, '.(()())...((((()()))((()(.()(((.)))()())))))()')
