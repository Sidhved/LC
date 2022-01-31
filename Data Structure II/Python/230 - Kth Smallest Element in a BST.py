# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []*k
        while True:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if k == 1:
                return root.val
            else:
                k -= 1
                root = root.right