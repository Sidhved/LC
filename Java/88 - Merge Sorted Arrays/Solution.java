class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if (n == 0)
            nums1 = nums1;
        else{
            for(int i = 0; i<n; i++){
                nums1[m+i] = nums2[i];
            }
            Arrays.sort(nums1);
        }
    }
}