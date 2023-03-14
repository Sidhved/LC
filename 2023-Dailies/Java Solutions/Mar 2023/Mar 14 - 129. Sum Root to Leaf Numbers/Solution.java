/**
 * Definition for a binary tree node.*/
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution {
    public int sumNumbers(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return sum(root, "");
    }
    private int sum(TreeNode root, String curr){
        if (root.left == null && root.right == null) {
            return Integer.parseInt(curr + root.val);
        }
        int sums = 0;
        if (root.left != null) {
            sums += sum(root.left, curr + root.val);
        }
        if (root.right != null) {
            sums += sum(root.right, curr + root.val);
        }
        return sums;
    }
}