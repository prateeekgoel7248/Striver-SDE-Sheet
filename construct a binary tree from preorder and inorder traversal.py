'''
Binary tree node class for reference
e

'''
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildBinaryTree(preorder:list, inorder:list):
        def buildingTree(preorder,preStart,preEnd,inorder,inStart,inEnd,d):
            if preStart>preEnd or inStart>inEnd:
                return None
            root = BinaryTreeNode(preorder[preStart])
            # print(root.val)
            ind = d[root.data]
            eleCount = ind-inStart
            root.left = buildingTree(preorder,preStart+1,preStart+eleCount,inorder,inStart,ind-1,d)
            root.right = buildingTree(preorder,preStart+eleCount+1,preEnd,inorder,ind+1,inEnd,d)
            return root
        d=dict()
        for i in range(len(inorder)):
            d[inorder[i]]=i
        root = buildingTree(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,d)
        return root