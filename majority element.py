from os import *
from sys import *
from collections import *
from math import *

def findMajorityElement(arr, n):
	# Write your code here.
	
        major=-1
        count=0
        for i in arr:
            if count==0:
                major=i
                count=1
            elif major==i:
                count+=1
            else:
                count-=1
        return major if arr.count(major)>n//2 else -1