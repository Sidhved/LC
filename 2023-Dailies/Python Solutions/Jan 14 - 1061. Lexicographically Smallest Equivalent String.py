class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        neighbors = collections.defaultdict(set)
        for a, b in zip(A, B):
            neighbors[a].add(b)
            neighbors[b].add(a)

        memo = {}

        def bfs(ch):
            if ch in memo: return memo[ch]
            res = ch
            seen = set()
            queue = {ch}

            while queue:
                c = queue.pop()
                if c in seen: continue
                seen.add(c)
                res = min(res, c)
                queue |= neighbors[c]

            for v in seen:
                memo[v] = res

            return res
        return ''.join(bfs(c) for c  in S)