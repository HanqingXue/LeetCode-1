"""
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode *root) {
        if(!root) return true; // if root == None: return true
        return helper(root->left, root->right); // recurse root leftside, root rightside)
    }
    bool helper(TreeNode *left, TreeNode *right){ // helper function(left, right)
        if(!left) return !right; //if self.left == None, return Not Right
        if(!right) return !left; // if self.right == None, return Not left
        
        if(left->val != right->val) return false; // if self.left.val != self.right.val, return False
        
        return helper(left->left, right->right) && helper(left->right, right->left); // recurse helper(self.left.left, self.right.right) [outside of the shit] & helper(self.left.right, self.right.right) [inside shit]
    }
};


Consider:
1. Empty tree?
2. Tree with only one node


"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root): 
        if root == None: #if there is no root the tree is symmetric
            return True
        return helper(root.left, root.right) #otherwise recuse using helper function(left subtree, right subtree)

def helper(left, right):
    if left == None: #if nothing in left subtree/node
        return not right #return NOT right
    if right == None: #if nothing in right subtree/node
        return not left #return not left
    if left.val != right.val: #if value of left != right value
        return False #return as false
    return helper(left.left, right.right) and helper(left.right, right.left) #recurse helper function