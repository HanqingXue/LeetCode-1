/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
 */
public class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null) return true; // A tree is balanced if it has no nodes
        
        int rHeight = height(root.right); // Find height of right side
        int lHeight = height(root.left); // Find height of left side
        
        // ABS minus is not greater than 1. And also every subtree is balanced, then return true;
        if (Math.abs(rHeight - lHeight) <= 1 && isBalanced(root.right) && isBalanced(root.left)) return true;
        else return false; // Otherwise one subtree isn't balanced then false
    }
    
    
    /* Helper function; finds height of tree (max Depth) */
    public int height(TreeNode root) {
        if (root == null) return 0; // No nodes means height is 0
        
        int lDepth = height(root.left); // Left side
        int rDepth = height(root.right); // Right side
        
        return 1 + Math.max(lDepth, rDepth); // Whichever side is bigger (i.e height)
    }
}
