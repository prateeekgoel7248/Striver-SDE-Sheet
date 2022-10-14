import sys
def ninjaAndLadoos(row1, row2, m, n, k):
    # Write your code here.
    if m<n: return ninjaAndLadoos(row2,row1,n,m,k)
    low=max(0,k-n)
    high=min(k,m)
    mn=-sys.maxsize
    mx=sys.maxsize
    while low<=high:
        cut1 = (low+high)//2
        cut2 = k-cut1
        l1 = mn if cut1==0 else row1[cut1-1]
        l2 = mn if cut2==0 else row2[cut2-1]
        r1 = mx if cut1==m else row1[cut1]
        r2 = mx if cut2==n else row2[cut2]
        if l1<=r2 and l2<=r1:
            return max(l1,l2)
        if l1>r2:
            high=cut1-1
        else:
            low=cut1+1
    return -1
        
        
        