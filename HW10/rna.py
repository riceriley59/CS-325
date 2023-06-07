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
        if start >= end:
            return 0, ''

        if best[(start, end)] != 0:
            return best[(start, end)], back[(start, end)]

        max_pairs = 0
        max_structure = ''

        if rna[start] in pairs[rna[end]]:
            pairs_count, structure = _best(start + 1, end - 1, best, back)
            max_pairs = pairs_count + 1
            max_structure = f'({structure})'

        for k in range(start, end):
            left_pairs, left_structure = _best(start, k, best, back)
            right_pairs, right_structure = _best(k + 1, end, best, back)

            if left_pairs + right_pairs > max_pairs:
                max_pairs = left_pairs + right_pairs
                max_structure = left_structure + right_structure

        best[(start, end)] = max_pairs
        back[(start, end)] = max_structure

        return max_pairs, max_structure

    max_pairs, max_structure = _best(0, n - 1, best, back)
    return max_pairs, max_structure

def total(rna: str) -> int:
    total, n = defaultdict(int), len(rna)

    return None

def kbest(rna: str, k: int) -> list[tuple]:
    return None

if __name__ == '__main__': 
    # Testing the provided examples
    print(best("ACAGU"))  # (2, '((.))')
    print(best("GCACG"))  # (2, '().()')
    print(best("UUCAGGA"))  # (3, '(((.)))')
    print(best("GUUAGAGUCU"))  # (4, '(.()((.)))')
    print(best("AUAACCUUAUAGGGCUCUG"))  # (8, '.(((..)()()((()))))')
    print(best("AACCGCUGUGUCAAGCCCAUCCUGCCUUGUU"))  # (11, '(((.(..(.((.)((...().))()))))))')
    print(best("GAUGCCGUGUAGUCCAAAGACUUCACCGUUGG"))  # (14, '.()()(()(()())(((.((.)(.))()))))')
    print(best("CAUCGGGGUCUGAGAUGGCCAUGAAGGGCACGUACUGUUU"))  # (18, '(()())(((((.)))()(((())(.(.().()()))))))')
    print(best("ACGGCCAGUAAAGGUCAUAUACGCGGAAUGACAGGUCUAUCUAC"))  # (19, '.()(((.)(..))(((.()()(())))(((.)((())))))())')
    print(best("AGGCAUCAAACCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA"))  # (20, '.(()())...((((()()))((()(.()(((.)))()())))))()')
