class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)
        if l % 2 == 0:
            h = l/2
        else:
            h = l//2
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in d:
            if d[i] > h:
                return i