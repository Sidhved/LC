import java.util.LinkedList;
import java.util.List;

class Solution {
    public List<Integer> addToArrayForm(int[] A, int K) {
        List<Integer> ans = new LinkedList<>();
        
        for(int i = A.length - 1; i >= 0 || K > 0; i--) {
            int sum = K;
            if(i >= 0) sum += A[i];
            
            // Use K as the carry digit
            ans.add(0, sum % 10);
            K = sum / 10;
        }
        
        return ans;
    }
}