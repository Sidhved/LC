# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        p = []
        q = []
        p.append(root)
        while True:
            last = root.val
            while p:
                if p[0].left:
                    q.append(p[0].left)
                if p[0].right:
                    q.append(p[0].right)
                last = p[0].val
                p.pop(0);
            res.append(last)
            p = q
            q = []
            if not p:
                return res
