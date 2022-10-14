'''
  ----Binary tree node class for reference-----
    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''

def getMaxWidth(root):

        if not root:
            return 0
        ans=0
        q= [root]
        while q:
            size = len(q)
            ans=max(ans,size)
            for i in range(size):
                temp = q.pop(0)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
        return ans