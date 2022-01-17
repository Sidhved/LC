class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = [[]]
        for c in s:
            if c.isalpha():
                for i in range(len(result)):
                    result.append(result[i][:])
                    result[i].append(c.lower())
                    result[-1].append(c.upper())
            else:
                for s in result:
                    s.append(c)
        return map("".join, result)