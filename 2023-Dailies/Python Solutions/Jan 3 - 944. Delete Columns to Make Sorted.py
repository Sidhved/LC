from ast import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum([1-(sorted(col)==list(col)) for col in zip(*strs)])