class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zeros = ones = 0
        for c in s:
            if c == '0':
                zeros += 1
            else:
                ones += 1
            zeros = min(zeros, ones)
        return zeros