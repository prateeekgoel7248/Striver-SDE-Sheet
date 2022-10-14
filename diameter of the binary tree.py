
# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diameterOfBinaryTree(root):
	# Write your code here
	# Return the root of the tree
	
    res=[0]
    def solve(root):
        if not root:
            return 0
        l=solve(root.left)
        r=solve(root.right)
        res[0]=max(res[0],l+r)
        return 1+max(l,r)
    solve(root)
    return res[0]