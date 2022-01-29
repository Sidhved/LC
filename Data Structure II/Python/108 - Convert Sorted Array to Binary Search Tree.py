# Definition for a binary tree node.
from ast import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.getHelper(nums, 0, len(nums) - 1)
    
    def getHelper(self, nums, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = TreeNode(nums[mid])
        node.left = self.getHelper(nums, start, mid - 1)
        node.right = self.getHelper(nums, mid + 1, end)
        return node