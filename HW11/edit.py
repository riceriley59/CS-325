from collections import defaultdict
import heapq

def distance1(s, t):
    m, n, dp = len(s), len(t), defaultdict(int)

    for i in range(m + 1): dp[(i, 0)] = i

    for j in range(n + 1): dp[(0, j)] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[(i, j)] = dp[(i - 1, j - 1)]
            else:
                dp[(i, j)] = 1 + min(dp[(i - 1, j)], dp[(i, j - 1)], dp[(i - 1, j - 1)])

    return dp[(m, n)]

def distance2(s, t):
    m, n = len(s), len(t)
    heap = [(0, 0, 0)]
    visited = set()

    while heap:
        dist, i, j = heapq.heappop(heap)

        if i == m and j == n: return dist

        if (i, j) in visited: continue

        visited.add((i, j))

        if i < m and j < n:
            if s[i] == t[j]:
                heapq.heappush(heap, (dist, i + 1, j + 1))
            else:
                heapq.heappush(heap, (dist + 1, i + 1, j + 1))

        if i < m: heapq.heappush(heap, (dist + 1, i + 1, j))

        if j < n: heapq.heappush(heap, (dist + 1, i, j + 1))

    return -1


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