import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if(root==null) return res;
        Queue<TreeNode> q = new LinkedList<>();
        boolean reverse=false;
        q.offer(root);
        while(!q.isEmpty()){
            int l = q.size(); 
            List<Integer> ll = new LinkedList<>();

            for(int i=0; i < l ; i++){
                
                TreeNode ln = q.poll();
                if(reverse) ll.add(0,ln.val);
                else ll.add(ln.val);
                if(ln.left!=null) q.offer(ln.left);
                if(ln.right!=null) q.offer(ln.right);
            
            }
            res.add(ll);
            reverse = reverse?false:true;
        }
        return res;
    }
}