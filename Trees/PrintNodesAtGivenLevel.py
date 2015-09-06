class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def PrintTreeLeve(t, desire): #No need to keep track of current level
    if (desire < 0): #check if desire level is valid
        return
        
    #define two queues, 1. store tree nodes,2. for current levels
    trees = []
    levels = []
    
    #start by pussing root node in the queue
    trees.append(t)
    levels.append(0) # start is level 0
    
    #now define a loop to continue while queue is not empty
    while trees != []:
        print(trees, levels)
        temp = trees.pop(0) # dequeue and store in temp
        currentLevel = levels.pop(0) # get the associated level
        if temp == None: # before proceeding if current tree node is nul
            return
        elif (currentLevel == desire):
            print(temp.value)
        else:
            trees.append(temp.left)
            levels.append(currentLevel + 1)
            trees.append(temp.right)
            levels.append(currentLevel + 1)

myTree = TreeNode(1)
myTree.left = TreeNode(2)
myTree.right = TreeNode(3)
myTree.left.left = TreeNode(4)
myTree.right.right = TreeNode(5)
myTree.left.right = TreeNode(6)
myTree.right.left = TreeNode(7)

PrintTreeLeve(myTree, 2)
