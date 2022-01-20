class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        mask = 1
        for i in range(0,32):
            if n & mask:
                res += 1
            if i != 31:
                res <<= 1
            mask <<= 1
        return res