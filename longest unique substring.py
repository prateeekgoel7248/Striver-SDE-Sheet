from os import *
from sys import *
from collections import *
from math import *

def uniqueSubstrings(s) :
    # Write you
    i=0
    j=0
    mx=0
    n=len(s)
    d=defaultdict(int)
    while j<n:
        d[s[j]]+=1
        if len(d)>j-i+1:
            j+=1
        elif len(d)==j-i+1:
            mx=max(mx,j-i+1)
            j+=1
        else:
            while len(d)<j-i+1:
                if d[s[i]]==1:
                    d.pop(s[i])
                else:
                    d[s[i]]-=1
                i+=1
            j+=1
    return mx
   
        