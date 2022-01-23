from typing import Collection, List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l, r = [], []
        if len(s) < 10: return []
        for i in range(len(s) - 9):
            l.extend([s[i:i + 10]])
        return [k for k, v in Collection.Counter(l).items() if v > 1]