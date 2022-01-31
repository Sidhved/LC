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

class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        TreeNode pre = null;
        TreeNode node = root;
        while (node != null) {
            if (node.val == key) {
                break;
            }
            pre = node;
            if (node.val > key) {
                node = node.left;
            }
            else {
                node = node.right;
            }
        }
        if (node == null) {
            return root;
        }
        if (pre == null) {
            return del(node);
        }
        if (pre.left == node) {
            pre.left = del(node);
        }
        else {
            pre.right = del(node);
        }
        return root;
    }
    private TreeNode del(TreeNode node) {
        if (node.left == null && node.right == null) {
            return null;
        }
        if (node.left == null) {
            return node.right;
        }
        if (node.right == null) {
            return node.left;
        }
        TreeNode pre = node;
        TreeNode curr = node.right;
        while (curr.left != null) {
            pre = curr;
            curr = curr.left;
        }
        node.val = curr.val;
        if (pre.left == curr) {
            pre.left = curr.right;
        }
        else {
            pre.right = curr.right;
        }
        return node;
    }
}