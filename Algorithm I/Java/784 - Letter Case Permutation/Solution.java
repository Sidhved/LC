import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> letterCasePermutation(String s) {
        List ans = new ArrayList();
        dfs(s.toLowerCase().toCharArray(), ans, 0, s.length());
        return ans;
    }
    public void dfs(char[] chArr, List ans, int i, int len) {
        if (i < len) {
            dfs(chArr, ans, i+1, len);
            if (Character.isLetter(chArr[i])) {
                chArr[i] = Character.toUpperCase(chArr[i]);
                dfs(chArr, ans, i+1, len);
                chArr[i] = Character.toLowerCase(chArr[i]);
            }
        } else ans.add(new String(chArr));
    }
}