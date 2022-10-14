def maximumActivities(start, finish):
    # Write your Code here.
    lis=list(zip(start,finish))
    lis.sort(key=lambda x:x[1])
    prev=0
    ans=1
    for cur in range(1,len(lis)):
        if lis[cur][0]>=lis[prev][1]:
            ans+=1
            prev=cur
    return ans