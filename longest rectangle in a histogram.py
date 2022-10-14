def largestRectangle(heights):
    # Write your code here.
        def nsr(arr):
            ans=[]
            stack=[]
            for i in range(len(arr)-1,-1,-1):
                while stack and stack[-1][1]>=arr[i]:
                    stack.pop()
                if not stack:
                    ans.append(len(arr))
                else:
                    ans.append(stack[-1][0])
                stack.append([i,arr[i]])
            return ans[::-1]
        def nsl(arr):
            ans=[]
            stack=[]
            for i in range(len(arr)):
                while stack and stack[-1][1]>=arr[i]:
                    stack.pop()
                if not stack:
                    ans.append(-1)
                else:
                    ans.append(stack[-1][0])
                stack.append([i,arr[i]])
            return ans
        mx=-1
        nslArr= nsl(heights)
        nsrArr= nsr(heights)
        # print(nslArr)
        # print(nsrArr)
        for i in range(len(heights)):
            mx=max(mx,heights[i]*(nsrArr[i]-nslArr[i]-1))
        return mx