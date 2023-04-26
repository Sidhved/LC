class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            result = 0
            for c in str(num):
                result += int(c)            
            num = result
       
        return num