# Following is the Binary Tree Node class structure
class BinaryTreeNode:
    
    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None
              
        
def identicalTrees(root1, root2):
    #Your code goes here.
    if not root1 or not root2:
        return root1==root2
    return root1.data==root2.data and identicalTrees(root1.left,root2.left) and identicalTrees(root1.right,root2.right)
    