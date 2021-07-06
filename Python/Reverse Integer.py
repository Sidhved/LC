'''Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
'''

class Solution:
    def reverse(self, x):
        r, p = 0, 1
        if x < 0:
            p = -1
            x = -1 * x
        while x > 0:
            r = r * 10 + x % 10
            if r > 2147483647:
                return 0
            x //= 10
        return r * p
        