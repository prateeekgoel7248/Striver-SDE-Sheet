from os import *
from sys import *
from collections import *
from math import *

# List Node Class.
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None

    def __del__(self):
        if(self.next):
            del self.next


def addTwoNumbers(l1, l2):
    # Write your code here.
    carry=0
    res=ans=Node(0)
    while l1 or l2 or carry:
        val1 = l1.data if l1 else 0
        val2 = l2.data if l2 else 0
        carry,out = divmod(val1+val2+carry,10)
        ans.next= Node(out)
        ans=ans.next
        l1=l1.next if l1 else None
        l2=l2.next if l2 else None
    return res.next