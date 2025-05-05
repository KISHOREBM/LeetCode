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
    boolean traverse(TreeNode p, TreeNode q){
        if(p==null && q==null)
        return true;
        if((p==null || q==null) || (p.val!=q.val))
        return false;
        if(!traverse(p.left,q.left)) return false;
        if(!traverse(p.right,q.right)) return false;
        return true;
    }
    public boolean isSameTree(TreeNode p, TreeNode q) {
        return traverse(p,q);
    }
}