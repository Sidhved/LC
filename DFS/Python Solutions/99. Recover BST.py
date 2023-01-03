# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pred = None
        x = None  # 1st wrong node
        y = None  # 2nd wrong node

        def findPredecessor(root: Optional[TreeNode]) -> Optional[TreeNode]:
            pred = root.left
            while pred.right and pred.right != root:
                pred = pred.right
            return pred

        while root:
            if root.left:
                morrisPred = findPredecessor(root)
                if morrisPred.right:  # Already connected before
          # Start the main logic
                    if pred and root.val < pred.val:
                        y = root
                        if not x:
                            x = pred
                    pred = root
          # End of the main logic
                    morrisPred.right = None  # Break the connection
                    root = root.right
                else:
                    morrisPred.right = root  # Connect it!
                    root = root.left
            else:
        # Start the main logic
                if pred and root.val < pred.val:
                    y = root
                    if not x:
                        x = pred
                pred = root
        # End of the main logic
                root = root.right

        def swap(x: Optional[TreeNode], y: Optional[TreeNode]) -> None:
            temp = x.val
            x.val = y.val
            y.val = temp

        swap(x, y)