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
    public int maxDepth(TreeNode root) {
        // Base Case
        if (root == null) return 0;
        
        // Recurse down
        else {
            // Left subtree Depth; keep track
            int lDepth = maxDepth(root.left);
            
            // Right subtree Depth; keep track
            int rDepth = maxDepth(root.right);
            
            // Return whichever is larger
            if (lDepth > rDepth) return (lDepth + 1);
            else return (rDepth + 1);
        }
    }
}
