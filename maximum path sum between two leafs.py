from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**7)


# Binary tree node class for reference.
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None



def findMaxSumPath(root):
    
    
    def solve(root,res):
        if not root:
            return 0
        l=solve(root.left,res)
        r=solve(root.right,res)
        temp = max(l,r)+root.val
        ans=max(temp,l+r+root.val)
        res[0]=max(res[0],ans)
        return temp
    res=[0]
    if not root:
        return -1
    if not root.left or not root.right:
        return -1
    
    solve(root,res)
    return res[0]
































# Taking level-order input using fast I/O method.
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    if length == 1:
        return None

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


# Main.
t = int(input())
for i in range(t):
    root = takeInput()
    maxSum = findMaxSumPath(root)
    print(maxSum)
