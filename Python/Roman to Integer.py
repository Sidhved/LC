'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        r = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        prev, total = 0, 0
        for i in s:
            curr = r[i]
            total += curr
            if curr > prev:
                total -= 2 * prev
            prev = curr
        return total
            


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("XXIV"))