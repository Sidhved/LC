class Solution {
    public int minFlipsMonoIncr(String s) {
        int flips = 0;
        int ones = 0;
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '0') {
                if (ones == 0) continue;
                else {
                    flips++;
                }
            } else {
                ones++;
            }
            
            if (flips > ones) {
                flips = ones;
            }
        }
        return flips;
    }
} 