from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def possible(piles, H, K):
            return sum((pile-1)//K+1 for pile in piles) <= H
        left, right = 1, max(piles)
        while left <= right:
            mid = left + (right-left)//2
            if possible(piles, H, mid):
                right = mid-1
            else:
                left = mid+1
        return left