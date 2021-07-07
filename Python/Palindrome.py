'''
Given an integer x, return true if x is palindrome integer.
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        r, t = 0, x
        if t < 0:
            return False
        while t != 0:
            r = r * 10 + t % 10
            t //= 10
        if r == x:
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(-121))