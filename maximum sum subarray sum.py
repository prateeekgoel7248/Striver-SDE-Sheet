from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :

        mx=0
        s=0
        for i in arr:
            s+=i
            mx=max(mx,s)
            if s<0:
                s=0
        return mx






























#taking inpit using fast I/O
def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
