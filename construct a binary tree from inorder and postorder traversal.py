'''

	Following is the TreeNode class structure


'''
class TreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None


def getTreeFromPostorderAndInorder(postorder, inorder):
        def solve(postorder,postStart,postEnd,inorder,inStart,inEnd,d):
            if postStart>postEnd or inStart>inEnd:
                return None
            root = TreeNode(postorder[postEnd])
            ind = d[root.data]
            eleCount = ind-inStart
            root.left = solve(postorder,postStart,postStart+eleCount-1,inorder,inStart,ind-1,d)
            root.right = solve(postorder,postStart+eleCount,postEnd-1,inorder,ind+1,inEnd,d)
            return root
        d=dict()
        for i in range(len(inorder)):
            d[inorder[i]]=i
        return solve(postorder,0,len(postorder)-1,inorder,0,len(inorder)-1,d)