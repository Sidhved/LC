from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        pairs = []
        for i in range(n):
            pairs.append((ages[i], scores[i]))
        pairs.sort(key = lambda x:(x[0], x[1]))
        dp = [0]*n
        for i in range(n):
            score_i = pairs[i][1]
            dp[i] = score_i
            for j in range(i):
                score_j = pairs[j][1]
                if score_j <= score_i:
                    dp[i] = max(dp[i], dp[j]+score_i)
        return max(dp)