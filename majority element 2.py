from os import *
from sys import *
from collections import *
from math import *

def majorityElementII(arr):
	# Write your code here.
        count1,count2,major1,major2=0,0,0,0
        for i in arr:
            if i==major1:
                count1+=1
            elif i==major2:
                count2+=1
            elif count1==0:
                count1+=1
                major1=i
            elif count2==0:
                count2+=1
                major2=i
            else:
                count1-=1
                count2-=1
        return [n for n in (major1,major2) if arr.count(n)>len(arr)//3]
    
    
    
    
    