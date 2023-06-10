def distance1(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]


def distance2(s, t):
    m, n = len(s), len(t)
    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 0

    for i in range(m + 1):
        for j in range(n + 1):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
            if i > 0 and j > 0:
                cost = 0 if s[i - 1] == t[j - 1] else 1
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + cost)

    return dp[m][n]

if __name__ == '__main__':
    print(distance1("abcdefh", "abbcdfg"))
    print(distance1("pretty", "prettier"))
    print(distance1("aaaaaaadaaaaaaaaaaaaaaaaacaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaxaaaaaaaaaaaaaaaaaaaaaa"))
    print(distance1('cpuyedzrwcbritzclzhwwabmlyresvewkdxwkamyzbxtwiqzvokqpkecyywrbvhlqgxzutdjfmvlhsezfbhfjbllmfhzlqlcwibubyyjupbwhztskyksfthkptxqlmhivfjbgclwsombvytdztapwpzmdqfwwrhqsgztobeuiatcwmrzfbwhfnpzzasomrhotoqiwvexlgxsnafiagfewmopdzwanxswfsmbxsmsczbwsgnwy', 'cpuyedzrwcbritzclzhwwabmlyresvewkdxwkamyzbtwiqzvokqpkecyywrbvhlqgxzutdjfmvlhsezfbhfjbllmfhzlqlcwibubyyjupbwhztskyksfthkptxqlmhivfbgclwsombvytdztapwpzmdqfwwrhqsgztobeuiatcwmrzfbwhfnpzzasonrhotoqiwvexlgxsnafiagfewmopdzwanxswfsmbxsmsczbwsgnwy'))
    print(distance1('cpuyedzrwcbritzclzhwwabmlyresvewkdxwkamyzbtwiqzvokqpasdfkecyywrbvhlqgxzutdjfmvlhsezfbhbllmfhzlqlcwibubyyjupbwhztsxyksfthkptxqlmhivfjbgclhombvytdztapwpzmdqfwwrhqsgztobeuiatcwmrzfbwhfnpzzasomrttoqiwvexlgxsnafiagfewmopdzwanxswfsmbxsmsczbwsgnwydmbihjkvziitusmkjljrsbafytsinql', 'cpuyedzrwcbritzclzhwwabmlyresvewkdxwkamyzbtwiqzvokqpkecyywrbvhlqgxzutdjfmvlhsezfbhfjbllmfhzlqlcwibubyyjupbwhztskyksfthkptxqlmhivfjbgclwsombvytdztapwpzmdqfwwrhqsgztobeuiatcwmrzfbwhfnpzzasomrhotoqiwvexlgxsnafiagfewmopdzwanxswfsmbxsmsczbwsgnwydmbihjkvziitusmkjljrsbafytsinql'))

    print(distance2("abcdefh", "abbcdfg"))
    print(distance2("pretty", "prettier"))
    print(distance2("aaaaaaadaaaaaaaaaaaaaaaaacaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaxaaaaaaaaaaaaaaaaaaaaaa"))
    print(distance2('cpuyedzrwcbritzclzhwwabmlyresvewkdxwkamyzbxtwiqzvokqpkecyywrbvhlqgxzutdjfmvlhsezfbhfjbllmfhzlqlcwibubyyjupbwhztskyksfthkptxqlmhivfjbgclwsombvytdztapwpzmdqfwwrhqsgztobeuiatcwmrzfbwhfnpzzasomrhotoqiwvexlgxsnafiagfewmopdzwanxswfsmbxsmsczbwsgnwy', 'cpuyedzrwcbritzclzhwwabmlyresvewkdxwkamyzbtwiqzvokqpkecyywrbvhlqgxzutdjfmvlhsezfbhfjbllmfhzlqlcwibubyyjupbwhztskyksfthkptxqlmhivfbgclwsombvytdztapwpzmdqfwwrhqsgztobeuiatcwmrzfbwhfnpzzasonrhotoqiwvexlgxsnafiagfewmopdzwanxswfsmbxsmsczbwsgnwy'))
    print(distance2('cpuyedzrwcbritzclzhwwabmlyresvewkdxwkamyzbtwiqzvokqpasdfkecyywrbvhlqgxzutdjfmvlhsezfbhbllmfhzlqlcwibubyyjupbwhztsxyksfthkptxqlmhivfjbgclhombvytdztapwpzmdqfwwrhqsgztobeuiatcwmrzfbwhfnpzzasomrttoqiwvexlgxsnafiagfewmopdzwanxswfsmbxsmsczbwsgnwydmbihjkvziitusmkjljrsbafytsinql', 'cpuyedzrwcbritzclzhwwabmlyresvewkdxwkamyzbtwiqzvokqpkecyywrbvhlqgxzutdjfmvlhsezfbhfjbllmfhzlqlcwibubyyjupbwhztskyksfthkptxqlmhivfjbgclwsombvytdztapwpzmdqfwwrhqsgztobeuiatcwmrzfbwhfnpzzasomrhotoqiwvexlgxsnafiagfewmopdzwanxswfsmbxsmsczbwsgnwydmbihjkvziitusmkjljrsbafytsinql'))