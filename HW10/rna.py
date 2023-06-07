from collections import defaultdict
import heapq

pairs = {'A': 'U', 'U': 'AG', 'C': 'G', 'G': 'CU'}

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

    max_pairs = best[(0, n - 1)]

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

    return max_pairs, ''.join(structure_string)

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
    pairs = {'A': 'U', 'U': 'AG', 'C': 'G', 'G': 'CU'}
    n = len(rna)
    best_structure = best(rna)[1]
    total_count = total(rna)

    # Create a priority queue to store the k-best structures
    pq = []

    def generate_k_best(start: int, end: int, prefix: str):
        if start >= end:
            pairs_count = prefix.count('(')
            pq.append((pairs_count, prefix))
            return

        if start + 1 == end:
            if rna[start] in pairs[rna[end]]:
                pq.append((1, prefix + "()"))
            pq.append((0, prefix + ".."))
            return

        if rna[start] in pairs[rna[end]]:
            generate_k_best(start + 1, end - 1, prefix + "()")

        generate_k_best(start, end - 1, prefix + ".")
        generate_k_best(start + 1, end, prefix + ".")

        for k in range(start + 1, end):
            if rna[start] in pairs[rna[k]]:
                left_count = best((rna[start:k + 1]))[0]
                right_count = best((rna[k + 1:end + 1]))[0]
                total_pairs = left_count + right_count
                generate_k_best(start, k, prefix + "(")
                generate_k_best(k + 1, end, prefix + ")")

    generate_k_best(0, n - 1, "")

    if k >= total_count:
        return pq[:total_count]

    # Sort the k-best structures by count in descending order
    pq.sort(reverse=True)

    return pq[:k]

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
        "AGGCAUCAAACCCUGCAUGGGAGCG",
        "CGAGGUGGCACUGACCAAACACCACCGAAAC"
    ]

    for s in test_cases:
        print(best(s))
        print(total(s))
        print(kbest(s, 10))
