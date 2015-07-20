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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        /* base cases */
        // Both are null (ending the same)
        if (p == null && q == null) return true;
        // If one ends before another (p or q hits null first)
        if (p == null || q == null) return false;
    
        /* Check p and q same data, Recurse left side, Recurse right side */
        return p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        
    }
}
