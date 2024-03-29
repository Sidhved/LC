# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        q = [root]
        while q and q[0] is not None:
            x = q.pop(0)
            q.append(x.left)
            q.append(x.right)
        while q:
            x = q.pop(0)
            if x is not None:
                return False
        return True