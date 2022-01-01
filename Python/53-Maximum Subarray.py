# 53 Maximum Subarray

#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

#A subarray is a contiguous part of an array.



#kadane's algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = len(nums)
        m = -999999999 - 1
        me = 0
        for i in range(s):
            me += nums[i]
            if m < me:
                m = me
            
            if me < 0:
                me = 0
        return m