class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        mydict = {char: count for count, char in enumerate(order)}
        
        for word1, word2 in zip(words[:-1], words[1:]):
            
            needtocomparelen = True
            for c1,c2 in zip(word1,word2):  # zip stops when one of them is used up 
                if mydict[c1] > mydict[c2]:
                    return False
                elif mydict[c1] < mydict[c2]:
                    needtocomparelen = False 
                    break
            
            if needtocomparelen and len(word1) > len(word2):
                return False

        return True