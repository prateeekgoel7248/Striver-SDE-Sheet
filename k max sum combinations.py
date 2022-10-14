from heapq import heappush,heappop
def kMaxSumCombination(a, b, n, k):
	# Write your code here.
            a.sort()
            b.sort()
            heap=[]
            ans=[]
            se=set()
            heappush(heap,[-(a[-1]+b[-1]),n-1,n-1])
            se.add((n-1,n-1))
            for i in range(k):
                temp = heappop(heap)
                ans.append(-temp[0])
                r = temp[1]
                c = temp[2]
                s=a[r-1]+b[c]
                if (r-1,c) not in se:
                    heappush(heap,[-s,r-1,c])
                    se.add((r-1,c))
                s=a[r]+b[c-1]
                if (r,c-1) not in se:
                    heappush(heap,[-s,r,c-1])
                    se.add((r,c-1))
#             print(heap)
            return ans
                

