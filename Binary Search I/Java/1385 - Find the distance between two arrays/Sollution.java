import java.util.Arrays;

class Solution {
    public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
        Arrays.sort(arr2);
        int ans = 0;
        for (int i= 0;i<arr1.length;i++) {
            int it = Arrays.binarySearch(arr2, 0, arr2.length, arr1[i]);
            if (it < 0) it = -(it+1);
            boolean isIt = false;
            if(it<arr2.length && Math.abs(arr2[it] - arr1[i]) <= d)isIt = true;
            if(it != 0 && Math.abs(arr2[it-1] - arr1[i]) <= d)isIt = true;
            if(!isIt)
                ans++;
        }
        return ans;
    }
}