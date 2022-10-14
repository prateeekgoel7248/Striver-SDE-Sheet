from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices):
    import sys
    mn=sys.maxsize
    mx=-sys.maxsize
    ans=0
    for i in prices:
        mn =min(mn,i)
#         mx=max(mx,i)
        ans = max(ans,i-mn)
    return ans
    # Write your code here.