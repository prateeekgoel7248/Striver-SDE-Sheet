def chessTournament(positions, n , c):
    positions.sort()
    def isPos(mid):
        s=0
        cnt=1
        prev=positions[0]
        for i in positions[1:]:
            s+=(i-prev)
            prev=i
            if s>=mid:
                s=0
                cnt+=1
            
        return cnt>=c
    low=1
    high=max(positions)
#     print(isPos(2))
    mx=0
    while low<high:
        mid=(low+high)//2
        if isPos(mid):
            mx=mid
            low=mid+1
        else:
            high=mid
    return mx
    
     
