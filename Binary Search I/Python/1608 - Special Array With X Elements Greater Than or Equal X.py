class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)  # Time: O(nlogn)
        for i in range(len(nums)):  # Time: O(n)
            if nums[i] <= i:
                break
        else:
            i += 1
        return -1 if i < len(nums) and nums[i] == i else i