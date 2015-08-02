/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        
        if (root.left == null && root.right == null) return 1;
        
        /* Remember that the MIN is different. If it has no subtree; it doesn't mean 0 */
        // No left subtree; go right.
        if (root.left == null && root.right != null) return minDepth(root.right) + 1;
        // No right subtree; go left.
        if (root.right == null && root.left != null) return minDepth(root.left) + 1;
        
        int rDepth = minDepth(root.right);
        int lDepth  = minDepth(root.left);
        
        return Math.min(lDepth, rDepth) + 1;
    }
}
