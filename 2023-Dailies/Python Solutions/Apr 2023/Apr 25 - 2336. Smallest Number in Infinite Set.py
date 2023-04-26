import bisect


class SmallestInfiniteSet:

    def __init__(self):
        self.Set = [i for i in range(1, 1001)]

    def popSmallest(self) -> int:
        if self.Set:
            v = self.Set[0]
            self.Set.pop(0)
        return v

    def addBack(self, num: int) -> None:
        if num in self.Set:
            return
        bisect.insort_left(self.Set, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)