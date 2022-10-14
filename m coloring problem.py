#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, m, n):
    def possible(node,color,n,col):
        for i in range(len(graph)):
            if graph[node][i] and color[i]==col:
                return False
        return True
    
    def solve(node,color,m,n):
        if node==n:
            return True
        for col in range(m):
            if possible(node,color,n,col):
                color[node]=col
                if(solve(node+1,color,m,n)):
                    return True
                color[node]=-1
                
        return False
    color=[-1 for _ in range(n)]
    # print(k,V)
    return 1 if solve(0,color,m,n) else 0
    
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1

# } Driver Code Ends