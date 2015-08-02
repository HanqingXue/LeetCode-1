/*
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9

to

     4
   /   \
  7     2
 / \   / \
9   6 3   1
*/
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
    public TreeNode invertTree(TreeNode root) {
        // Edge case
        if (root == null) return root;
        
        // Swap left and right
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
        
        // Recursively do it for the LEFT subtree and RIGHT subtree
        this.invertTree(root.left);
        this.invertTree(root.right);
        
        return root;
        
    }
}
