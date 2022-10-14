from typing import *
from collections import defaultdict
class Trie:
    def __init__(self):
        self.child = defaultdict(Trie)
    def insert(self,num):
        cur = self
        for i in range(31,-1,-1):
            bit = (num>>i)&1
            cur = cur.child[bit]
    def getMax(self,num):
        cur = self
        mxNum=0
        for i in range(31,-1,-1):
            bit = (num>>i)&1
            if 1-bit in cur.child:
                mxNum = mxNum | (1<<i)
                cur = cur.child[1-bit]
            else:
                cur = cur.child[bit]
        return mxNum

def maxXorQueries(arr, queries):
    trie = Trie()
    arr.sort()
    offQ=[]
    for i in range(len(queries)):
        offQ.append([queries[i][1],queries[i][0],i])
    offQ.sort(key=lambda x:x[0])
    ind=0
    n=len(arr)
    ans=[-1 for _ in range(len(queries))]
    for i in range(len(offQ)):
        ai=offQ[i][0]
        xi = offQ[i][1]
        qInd  = offQ[i][2]
        while ind<n and arr[ind]<=ai:
            trie.insert(arr[ind])
            ind+=1
        if ind!=0:
            ans[qInd]=trie.getMax(xi)
    return ans
            
    


