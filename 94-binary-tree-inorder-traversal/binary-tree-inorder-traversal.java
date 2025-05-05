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
    void inorderTraverse(TreeNode root,List<Integer> lis){
        if(root == null) return;
        inorderTraverse(root.left,lis);
        lis.add(root.val);
        inorderTraverse(root.right,lis);
    }
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> lis = new ArrayList<>();
        inorderTraverse(root,lis);
        return lis;
    }
}