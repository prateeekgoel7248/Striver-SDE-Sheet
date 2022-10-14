def kthPermutation(n, k):

    # Write your code here.
    k-=1
    fact=1
    nums=[]
    ans=""
    for i in range(1,n):
        nums.append(i)
        fact*=i
    nums.append(n)
    for m in range(n-1,0,-1):
        ind = k//fact
        ans+=str(nums[ind])
        nums.pop(ind)
        k%=fact
        fact//=m
    ans+=str(nums[0])
    return int(''.join(ans))
        
    