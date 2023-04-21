class Solution {
    public int profitableSchemes(int G, int P, int[] group, int[] profit) {
        int mod = (int)1e9 + 7, n = group.length;
        long[][] dp = new long[1 + P][1 + G];
        dp[0][0] = 1;

        for(int i = 0; i < n; i++) {
            for(int j = P; j >= 0; j--) {
                for(int k = G - group[i]; k >= 0; k--) {
                    int newP = Math.min(j + profit[i], P);
                    int newG = k + group[i];
                    dp[newP][newG] = (dp[newP][newG] + dp[j][k]) % mod;
                }
            }
        }

        long ans = 0;
        for(int j = 0; j <= G; j++) {
            ans = (ans + dp[P][j]) % mod;
        }
        return (int)ans;
    }
}