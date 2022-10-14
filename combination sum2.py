def combinationSum2(arr, n, target):
    arr.sort()
    ans=[]
    def solve(ind,temp,rem):
        if rem==0:
            ans.append(((temp)))
            return
        for i in range(ind,len(arr)):
            if i>ind and arr[i]==arr[i-1]:
                continue
            if arr[i]>rem:
                break
            solve(i+1,temp+[arr[i]],rem-arr[i])
        
    temp=[]
    solve(0,temp,target)
#     print(len(ans),"ans")
    return ans