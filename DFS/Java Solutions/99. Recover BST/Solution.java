/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public void recoverTree(TreeNode root) {
        TreeNode pred = null;
        TreeNode x = null; // 1st wrong node
        TreeNode y = null; // 2nd wrong node

        while (root != null) {
            if (root.left == null) {
        // Start the main logic
                if (pred != null && root.val < pred.val) {
                    y = root;
                    if (x == null)
                        x = pred;
                }
                pred = root;
        // End of the main logic
                root = root.right;
                } 
                else {
                    TreeNode morrisPred = findPredecessor(root);
                    if (morrisPred.right == null) {
                        morrisPred.right = root; // Connect it!
                        root = root.left;
                    } 
                    else { // Already connected before
          // Start the main logic
                        if (pred != null && root.val < pred.val) {
                            y = root;
                            if (x == null)
                                x = pred;
                        }
                        pred = root;
          // End of the main logic
                        morrisPred.right = null; // Break the connection
                        root = root.right;
                    }
                }
        }

        swap(x, y);
    }

    private TreeNode findPredecessor(TreeNode root) {
        TreeNode pred = root.left;
        while (pred.right != null && pred.right != root)
            pred = pred.right;
        return pred;
    }

    private void swap(TreeNode x, TreeNode y) {
        final int temp = x.val;
        x.val = y.val;
        y.val = temp;
    }
}