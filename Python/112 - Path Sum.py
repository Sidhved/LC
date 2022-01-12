# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], sum: int) -> bool:
        if not root:
            return False
        else:
            sum = sum - root.val
            if not root.left and not root.right:
                if sum==0:
                    return True
            return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)