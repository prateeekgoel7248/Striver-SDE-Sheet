from collections import defaultdict
class Trie:
    def __init__(self):
        # Write your code here.
        self.child = defaultdict(Trie)
        self.ew=0
        self.cw=0

    def insert(self, word):
        cur = self
        for i in word:
            cur=cur.child[i]
            cur.cw+=1
        cur.ew+=1

    def countWordsEqualTo(self, word):
        cur = self
        for i in word:
            if i not in cur.child:
                return 0
            cur = cur.child[i]
        return cur.ew
                

    def countWordsStartingWith(self, word):
        cur = self
        for i in word:
            if i not in cur.child:
                return 0
            cur = cur.child[i]
        return cur.cw

    def erase(self, word):
        cur = self
        for i in word:
            if i not in cur.child:
                return 0
            cur = cur.child[i]
            cur.cw -=1
            
        cur.ew-=1