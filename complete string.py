from typing import *
from collections import defaultdict
class Trie:
    def __init__(self):
        self.child = defaultdict(Trie)
        self.end = False
    def insert(self,word):
        cur=self
        for i in word:
            cur=cur.child[i]
        cur.end=True
    def search(self,word):
        cur=self
        for i in word:
            if i not in cur.child:
                return False
            cur = cur.child[i]
        return cur.end
    def checkLongest(self,word):
        cur = self
        for i in word:
            cur=cur.child[i]
            if not cur.end:
                return False
        return True
                
        
def completeString(n: int, a: List[str])-> str:
    trie = Trie()
    for i in a:
        trie.insert(i)
    ans=""
    for i in a:
        if trie.checkLongest(i):
            if len(ans)<=len(i):
                ans=i
    if ans=="":
        return None
    return ans
            
        
    
    