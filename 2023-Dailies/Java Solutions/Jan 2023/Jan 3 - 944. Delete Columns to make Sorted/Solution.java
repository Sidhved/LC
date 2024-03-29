class Solution {
    public int minDeletionSize(String[] strs) {
        if(strs == null || strs.length == 0)
            return 0;

        int res = 0;
        int n = strs[0].length();

        for(int i = 0; i < n; i++) {
            int j = 0;
            for(; j < strs.length - 1; j++) {
                if(strs[j].charAt(i) > strs[j + 1].charAt(i)) {
                    break;
                }
            }

            if(j != strs.length - 1)
                res++;
        }

        return res;
    }
}