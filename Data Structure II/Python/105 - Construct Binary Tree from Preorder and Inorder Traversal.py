# Definition for a binary tree node.
from ast import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        return self.create_tree(inorder, 0, len(inorder) - 1, preorder, 0, len(preorder) - 1)
    def search_divindex(self, inorder, low_inorder, high_inorder, val):
        for i in range(low_inorder, high_inorder+1):
            if inorder[i] == val:
                return i
        return -1
    def create_tree(self, inorder, low_inorder, high_inorder, preorder, low_preorder, high_preorder):
        if (low_preorder > high_preorder) or (low_inorder > high_inorder):
            return None

        root = TreeNode(preorder[low_preorder])
        div_index = self.search_divindex(inorder, low_inorder, high_inorder, root.val)
        size_left_subtree = div_index - low_inorder
        size_right_subtree = high_inorder - div_index

        root.right = self.create_tree(inorder, div_index + 1, high_inorder, preorder, low_preorder + 1 + size_left_subtree, low_preorder + size_left_subtree + size_right_subtree)

        root.left = self.create_tree(inorder, low_inorder, div_index - 1, preorder, low_preorder + 1, low_preorder + size_left_subtree)

        return root