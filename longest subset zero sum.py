from os import *
from sys import *
from collections import *
from math import *

def LongestSubsetWithZeroSum(arr):

    # Write your Code here.
    # Return an integer denoting the answer.
    s=0
    d=defaultdict(int)
    mx=0
    for i in range(len(arr)):
        s+=arr[i]
        if s==0:
            mx=i+1
            continue
        if s in d:
            l = i-d[s]
            mx=max(mx,l)
        else:
            d[s]=i
    return mx