from typing import List
from heapq import *
from collections import *
def KMostFrequent(n: int, k: int, arr: List[int]) -> List[int]:
    # write your code here
    heap=[]
    d=Counter(arr)
    for i,j in d.items():
        heappush(heap,[-j,i])
        
    lis=[]
    for _ in range(k):
        temp=heappop(heap)
        lis.append(temp[1])
    return sorted(lis)
