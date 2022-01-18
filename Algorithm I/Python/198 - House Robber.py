class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        a = []
        a.append(nums[0])
        a.append(max(nums[0], nums[1]))
        for i in range(2, n):
            a.append(max(nums[i]+a[i-2], a[i-1]))
            
        return a[n-1]