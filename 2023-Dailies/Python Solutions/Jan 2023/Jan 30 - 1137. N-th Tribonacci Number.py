class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0,1,1]+[0 for _ in range(3,n+1)]
        for x in range(3,n+1):
            dp[x] = dp[x-1]+dp[x-2]+dp[x-3]
        return dp[n]