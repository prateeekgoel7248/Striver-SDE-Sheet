from os import *
from sys import *
from collections import *
from math import *

def lengthOfLongestConsecutiveSequence(arr, n):
    # Write your code here.
    s=set(arr)
    mxl=0
    hl = n//2
    for i in arr:
        cnt=1
        if i-1 not in s:
            while i+cnt in s:
                cnt+=1
            mxl = max(mxl,cnt)
            if mxl>hl:
                return mxl
    return mxl
            
