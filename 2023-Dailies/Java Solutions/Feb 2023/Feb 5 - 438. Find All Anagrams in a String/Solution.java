class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> rst = new ArrayList<>();
        if (s == null || s.length() == 0 || s.length() < p.length()) {
            return rst;
        }
        if (s.length() == p.length() && isAnagram(s, p)) {
            rst.add(0);
            return rst;
        }

        int i = 0;
        int j = p.length();
        while (j <= s.length()) {
            if (isAnagram(s.substring(i, j), p)) {
                rst.add(i);
            }
            i++;
            j++;
        }
        
        return rst;
    }
    
    private boolean isAnagram(String a, String b) {
        int[] arr = new int[26];
        for (int i = 0; i < a.length(); i++) {
            arr[a.charAt(i) - 'a']++;
            arr[b.charAt(i) - 'a']--;
        }
        for (int i = 0; i < 26; i++) {
            if (arr[i] != 0) {
                return false;
            }
        }
        return true;
    }
}