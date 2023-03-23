class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        uf = {i: i for i in range(n)}

        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(a, b):
            uf[find(a)] = find(b)

        if len(connections) < n - 1:
            return -1
        for a, b in connections:
            union(a, b)
        islands = len({find(x) for x in uf})
        return islands - 1