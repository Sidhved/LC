class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end - 1] = nums[end - 1], nums[start]
                start += 1
                end -= 1

        k %= len(nums)
        reverse(nums, 0, len(nums))
        reverse(nums, 0, k)
        reverse(nums, k, len(nums))