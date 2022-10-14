def ayushGivesNinjatest(m, n, time):
    # Write your code here.
    def isPos(mx):
        cnt=1
        s=0
        for i in time:
            s+=i
            if s>mx:
                cnt+=1
                s=i
        return cnt<=m
            
    low=max(time)
    high=sum(time)
    mn=high
    while low<high:
        mid=(low+high)//2
        if isPos(mid):
            mn=mid
            high=mid
        else:
            low=mid+1
    return mn
    