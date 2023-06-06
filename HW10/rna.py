def best(rna: str) -> tuple: 
    n = len(rna)
    dp = [[(0, '') for _ in range(n)] for _ in range(n)]

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if length == 1:
                dp[i][j] = (0, '.')
            else:
                best_score = dp[i][j - 1][0]
                best_structure = dp[i][j - 1][1] + '.'

                if (rna[j - 1] == 'A' and rna[j] == 'U') or (rna[j - 1] == 'U' and rna[j] == 'A') \
                        or (rna[j - 1] == 'G' and rna[j] == 'C') or (rna[j - 1] == 'C' and rna[j] == 'G') \
                        or (rna[j - 1] == 'G' and rna[j] == 'U') or (rna[j - 1] == 'U' and rna[j] == 'G'):
                    if dp[i][j - 1][0] < dp[i + 1][j - 1][0] + 1:
                        best_score = dp[i + 1][j - 1][0] + 1
                        best_structure = '(' + dp[i + 1][j - 1][1] + ')'

                for k in range(i, j - 1):
                    if dp[i][k][0] + dp[k + 1][j][0] > best_score:
                        best_score = dp[i][k][0] + dp[k + 1][j][0]
                        best_structure = dp[i][k][1] + dp[k + 1][j][1]

                dp[i][j] = (best_score, best_structure)

    return dp[0][n - 1]


def total(rna: str) -> int: 
    return None

def kbest(rna: str, k: int) -> list[tuple]: 
    return None