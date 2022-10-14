'''
  ----Binary tree node class for reference-----
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''


def isBalancedBT(root):

    def dfs(root):
        if not root:
            return 0
        l=dfs(root.left)
        if l==-1:
            return -1
        r=dfs(root.right)
        if r==-1:
            return -1
        if abs(l-r)>1:
            return -1
        return max(l,r)+1
    return dfs(root)!=-1
