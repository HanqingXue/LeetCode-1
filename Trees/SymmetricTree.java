/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 
/*Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following is not:

    1
   / \
  2   2
   \   \
   3    3
*/
public class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;
        return helper(root.left, root.right);
    }
    
    public boolean helper(TreeNode left, TreeNode right){
        // If the left side has no node but right does; or vice versa then FALSE
        if ((left==null && right!=null) || (left!=null && right==null))return false;
        
        // If passed in a leaf then TRUE 
        if(left==null && right==null) return true;
        
        // If node values aren't the same
        // Gotta check if LEAF first then you can do this step
        if (left.val != right.val) return false;
        
        return helper(left.left,right.right) && helper(left.right,right.left);
     }
}
