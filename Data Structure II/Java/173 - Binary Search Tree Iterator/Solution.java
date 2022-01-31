import java.util.Stack;

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

class BSTIterator {


    Stack<TreeNode> helper = new Stack<TreeNode>();
    public BSTIterator(TreeNode root) {
        while (root != null) {
            helper.push(root);
            root = root.left;
        }
    }
        
    public boolean hasNext() {
        return helper.size() != 0;
    }

    
    public int next() {
        TreeNode result = helper.pop();
        TreeNode node = result.right;
        while (node != null) {
            helper.push(node);
            node = node.left;
        }
        return result.val;
    }
    
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */