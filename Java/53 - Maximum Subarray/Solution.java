// 53 Maximum Subarray

// Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

// A subarray is a contiguous part of an array.

class Solution {
    public int maxSubArray(int[] nums) {
        int m = -999999 -1;
        int me = 0;
        
        for(int i = 0; i < nums.length; i++){
            me = me + nums[i];
            if(m<me){
                m = me;
            }
            
            if(me<0){
                me = 0;
            }
        }
        return m;
    }
}