class Solution:
    def partition(self, s: str) -> List[List[str]]:
        Solution.ans = []
        self.dfs(s, [])
        return Solution.ans
    
    def dfs(self, s, stringlist):
        if len(s) == 0:
            Solution.ans.append(stringlist)
        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], stringlist + [s[:i]])
    def isPalindrome(self, s):
        for i in range(len(s)):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True