from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        m = min(salary)
        m += max(salary)
        s = sum(salary) - m
        ans = s/(len(salary) - 2)
        return round(ans, 5)