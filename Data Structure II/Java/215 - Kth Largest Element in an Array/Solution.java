import java.util.Arrays;

class Solution {
    public int findKthLargest(int[] a, int k) {
        int n = a.length;
        Arrays.sort(a);
        return a[n - k];
    }
}