from sys import stdin, setrecursionlimit
import queue
import sys
from collections import OrderedDict
setrecursionlimit(10**6)
from collections import *

# Following is the structure used to represent the Binary Tree Node.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

	
def bottomView(root):
    
    q=[]
    if not root:
        return q
    q.append([root,0])
    d=defaultdict(int)
    while q:
        temp = q.pop(0)
        first = temp[0]
        second = temp[1]
        d[second]=first.data
        if first.left:
            q.append([first.left,second-1])
        if first.right:
            q.append([first.right,second+1])
    res=[]
    for i in sorted(d.keys()):
        res.append(d[i])
    return res


# Taking level-order input using fast I/O method.
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    if length == 1:
        return None

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
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
while t:
    root = takeInput()
    answer = bottomView(root)
    print(*answer)
    t = t - 1
