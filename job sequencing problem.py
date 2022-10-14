def jobScheduling(jobs):

    # Write your code here
    # Return an integer denoting the maximum pofit  
    jobs = sorted(jobs,key=lambda x:x[1],reverse=True)
    maxDead = 0
    for i in jobs:
        maxDead=max(maxDead,i[0])
#     print(maxDead,"md")
    profit=0
    seq=[-1]*(maxDead+1)
    for i in range(len(jobs)):
        for j in range(jobs[i][0],0,-1):
            if seq[j]==-1:
                seq[j]=1
                profit+=jobs[i][1]
                break
    return profit