import collections


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g, res = collections.defaultdict(list), [0] * n
        for (a, b) in edges:
            g[a].append(b)
            g[b].append(a)
        def dfs(i, last, g, labels, res):
            cnt = collections.Counter()
            for nei in g[i]:
                if nei == last: continue
                cnt += dfs(nei, i, g, labels, res)
            cnt[labels[i]] += 1
            res[i] = cnt[labels[i]]
            return cnt

        dfs(0, -1, g, labels, res)
        return res