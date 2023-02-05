from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
        m, n = len(s), len(p)
        if m < n:
            return answer
        pCounter = Counter(p)
        sCounter = Counter(s[:n-1])

        index = 0
        for index in range(n - 1, m):
            sCounter[s[index]] += 1
            if sCounter == pCounter:
                answer.append(index - n + 1)
            sCounter[s[index - n + 1]] -= 1
            if sCounter[s[index - n + 1]] == 0:
                del sCounter[s[index - n + 1]]
        return answer