class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};


class Solution {
    public Node connect(Node root) {
        if(root == null) return root;
        Node dummy = new Node(0);
        dummy.next = root;
        Node pre = root;
        while(root.left != null){
            Node preRight = null;
            while(root != null){
                if(preRight != null) preRight.next = root.left;
                root.left.next = root.right;
                preRight = root.right;
                root = root.next;
            }
            root = pre.left;
            pre = root;
        }
        return dummy.next;
    }  
}