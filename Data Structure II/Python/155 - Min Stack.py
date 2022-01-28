class MinStack:

    def __init__(self):
        self.stk = []
        self.non_asc = []

    def push(self, x: int) -> None:
        self.stk.append(x)
        if len(self.non_asc) == 0 or x <= self.non_asc[-1]:  # rather than <
            self.non_asc.append(x)


    def pop(self) -> None:
        x = self.stk.pop()
        if x == self.non_asc[-1]:
            self.non_asc.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.non_asc[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()