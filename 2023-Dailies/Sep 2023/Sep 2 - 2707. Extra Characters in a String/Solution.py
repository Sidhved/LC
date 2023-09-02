# Dynamic approach with substring manipulation

from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        max_val = len(s)+1
        dic_set = set(dictionary)
        dp = [max_val]*(len(s)+1)
        dp[0]=0
        for i in range(1,len(s)+1):
            dp[i] = dp[i-1]+1   #worst case scenario
            
            for j in range(1,i+1):
                if s[i-j:i] in dic_set:
                    dp[i] = min(dp[i], dp[i-j])
        return dp[-1]
    

# Dynamic Programming with Trie

class TrieNode:
    def __init__(self):
        self.children={}
        self.is_word=False
        
def buildTrie(dictionary):
    root = TrieNode()
    for words in dictionary:
        node = root
        for ch in words:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word=True
    return root

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = buildTrie(dictionary)
        n = len(s)
        dp = [float('inf')]*(n+1)
        dp[-1] = 0 # no character for empty string
        for start in reversed(range(n)):
            dp[start] = dp[start + 1] + 1  # Initialize with worst-case scenario
            node = root
            for end in range(start, n):
                if s[end] not in node.children:
                    break
                node = node.children[s[end]]
                if node.is_word:
                    dp[start] = min(dp[start], dp[end + 1])
        
        return dp[0]
        