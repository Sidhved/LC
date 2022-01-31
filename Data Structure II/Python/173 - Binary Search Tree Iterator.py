# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        current = root
        while current != None:
            self.stack.append(current)
            current = current.left
        return

    def next(self) -> int:
        next_node = self.stack.pop()
        current = next_node.right
        while current != None:
            self.stack.append(current)
            current = current.left
        return next_node.val

    def hasNext(self) -> bool:
        return len(self.stack) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()