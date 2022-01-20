class Solution:
    def int(self, n):
        return ord(n) - ord("0")
    def addStrings(self, num1: str, num2: str) -> str:
        ret = []
        # let num2 to be one has more digit
        if len(num1) > len(num2):
            num1, num2 = num2, num1

        num1 = num1[::-1]
        num2 = num2[::-1]
        carry = 0
        idx = 0
        while idx < len(num2):
            if idx < len(num1):
                s = self.int(num1[idx]) + self.int(num2[idx]) + carry
            else:
                s = self.int(num2[idx]) + carry

            if s >= 10:
                s -= 10
                carry = 1
            else:
                carry = 0

            ret.append(s)
            idx += 1

        if carry:
            ret.append(carry)

        return "".join(map(str, ret[::-1]))