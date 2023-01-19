class Solution {
    public int subarraysDivByK(int[] A, int K) {
        int[] map = new int[K];
        map[0] = 1;
        int count = 0, sum = 0;
        for (int a : A) {
            sum = (sum + a) % K;
            if (sum < 0) sum += K;
                map[sum]++;
        }
        for (int m : map) {
            if (m == 0) continue;
            count += m * (m - 1) / 2;
        }
        return count;
    }
}