/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
 
 /*
 Solution 1: Do an inorder traversal and check if the list is sorted.
 */
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: True if the binary tree is BST, or false
     */
    public boolean isValidBST(TreeNode root) {
        List<Integer> unfolded = new ArrayList<Integer>();
        inOrder(root, unfolded);
        //Integer[] array = unfolded.toArray();
        for (int i = 1; i < unfolded.size(); i++)
        if (unfolded.get(i-1) >= unfolded.get(i)) return false;
        return true;
        
    }
    
    public void inOrder(TreeNode node, List<Integer> listToAdd) {
    if(node != null)    {
       inOrder(node.left, listToAdd);
       listToAdd.add(node.val);
       inOrder(node.right, listToAdd);
    }
}
}
