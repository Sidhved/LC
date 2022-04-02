public class Solution {
    public int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length;
            
        while(start<end){
            int mid = ((end-start)/2) + start;
                
            if (nums[mid] == target){
                return mid;
            }
            else if(nums[mid] >target){
                end = mid;
            }
            else if(nums[mid]<target){
                start = mid + 1;
            }
        }
        return -1;
    }
}