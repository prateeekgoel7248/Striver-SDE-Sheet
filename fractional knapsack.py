def maximumValue(items, n, w):

	# Write your code here.
	# ITEMS contains [weight, value] pairs.
        items.sort(key=lambda x: -x[1]/x[0])
        res=0
        for i in range(n):
            if w>=items[i][0]:
                res+=items[i][1]
                w-=items[i][0]
            else:
                res+=(items[i][1]*(w/items[i][0]))
                break
        return res
                
            