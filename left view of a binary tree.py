# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getLeftView(root)->list:
    # Write your code here
    # Return a list
    ans=[]
    def solve(root,level):
        if not root:
            return 
        if level==len(ans):
            ans.append(root.data)
        solve(root.left,level+1)
        solve(root.right,level+1)
    solve(root,0)
    return ans