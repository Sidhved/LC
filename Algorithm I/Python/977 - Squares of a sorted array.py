class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s = [x**2 for x in nums]
        s = (sorted(s))
        return s