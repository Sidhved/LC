class Solution:
    def arrangeCoins(self, n: int) -> int:
        def check(mid, n):
            return mid*(mid+1) <= 2*n

        left, right = 1, n
        while left <= right:
            mid = left + (right-left)//2
            if not check(mid, n):
                right = mid-1
            else:
                left = mid+1
        return right