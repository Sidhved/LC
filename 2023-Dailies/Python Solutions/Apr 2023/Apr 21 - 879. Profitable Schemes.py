from typing import List


class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        # dp[g][p]
        dp = [[0]*(G+1) for i in range(P+1)]
        dp[0][0] = 1
        for g, p in zip(group, profit):
            for i in range(P, -1, -1):
                for j in range(G-g, -1, -1):
                    dp[min(P, i+p)][j+g] += dp[i][j] 
        return sum(dp[P])%(10**9+7)