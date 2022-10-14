# Following is the Binary Tree node structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def traverseBoundary(root):
    # Write your code here.
    res=[]
    def isLeaf(root):
        if root.left or root.right:
            return False
        return True
    def addLeft(root):
        temp=root.left
        while temp:
            if not isLeaf(temp):
                res.append(temp.data)
            if temp.left:
                temp=temp.left
            else:
                temp=temp.right
    def addRight(root):
        ans=[]
        temp=root.right
        while temp:
            if not isLeaf(temp):
                ans.append(temp.data)
            if temp.right:
                temp=temp.right
            else:
                temp=temp.left
        res.extend(ans[::-1])
    def addLeafs(root):
        if isLeaf(root):
            res.append(root.data)
        if root.left:
            addLeafs(root.left)
        if root.right:
            addLeafs(root.right)
    if not root:
        return res
    if not isLeaf(root):
#         print("Hello")
        res.append(root.data)
    addLeft(root)
    addLeafs(root)
    addRight(root)
    return res
            
            
        
        
