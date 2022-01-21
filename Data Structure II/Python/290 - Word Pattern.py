class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_groups = defaultdict(list)
        for i, c in enumerate(pattern):
            pattern_groups[c].append(i)
            
        word_groups = defaultdict(list)
        words = s.split()
        for i, word in enumerate(words):
            word_groups[word].append(i)
            
        return list(pattern_groups.values()) == list(word_groups.values())