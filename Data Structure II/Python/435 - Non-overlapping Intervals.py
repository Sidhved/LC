from cmath import inf


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        a = 0
        e = -inf

        for interval in sorted(intervals, key=lambda x: x[1]):
            if interval[0] >= e:
                e = interval[1]
            else:
                a += 1

        return a