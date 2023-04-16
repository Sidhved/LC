import collections
from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9+7
        # dp[i+1][j+1]: number of ways of target[0..j] using count[0..i].
        dp = [[0]*(len(target)+1) for _ in range(2)]
        for i in range(len(dp)):
            dp[i][0] = 1
        for i in range(len(words[0])):
            count = collections.Counter(w[i] for w in words)
            for j in reversed(range(len(target))):
                dp[(i+1)%2][j+1] = dp[i%2][j+1]+dp[i%2][j]*count[target[j]] % MOD
        return dp[(len(words[0]))%2][-1] % MOD