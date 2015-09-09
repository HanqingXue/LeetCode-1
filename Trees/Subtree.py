class BinaryTree:
    def __init__(self, k):
        self.value = k
        self.left = None
        self.right = None

def subtreeRef(t1, t2):
    # if t1 or t2 are null before comparing
    if t2 == None:
        return True
    if t1 == None:
        return False
        
    #otherwise we compare if they are equal reference at this moment if not compare t1's child with t2's child
    return (t1 == t2) or subtreeRef(t1.left, t2) or subtreeRef(t1.right, t2)
    
# check if subtrees are equal in value
def subtreeValue(t1, t2):
    #in this case we need firstly to check if root values are equal, if so we continute to check children values
    #for both trees until we find a match or not, this step should be tried until a true is returned or all the subtrees have been visted for t1
    
    #firstly ewe check if t2 == null
    if t2 == None:
        return True
    
    if t1 == None:
        return False
        
    if t1.value == t2.value:
        # the we need to check if both t1 and t2s subtrees are the same
        if subtreeValue(t1.left, t2.left) and subtreeValue(t1.right, t2.right):
            return True # we found one if roots are same s all children trees are the same
    else:
        #otherwise we need to go to t1's left or right subtree to continue the equality checking
        return subtreeValue(t1.left, t2) or subtreeValue(t1.right, t2)
        
t1 = BinaryTree(1)
t1.left = BinaryTree(2)
t1.right = BinaryTree(3)
t1.left.right = BinaryTree(4)
t1.right.left = BinaryTree(5)

t2 = BinaryTree(3)
t2.left = BinaryTree(4)
t2.right = BinaryTree(5)

print(subtreeRef(t1, t2) and subtreeValue(t1, t2))
