def graphColoring(graph,m):
    
    def possible(node,color,n,col):
        for i in range(len(graph[node])):
            if graph[node][i]!=0 and color[i]==col:
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
    
    n=len(graph)
    color=[-1 for _ in range(n)]
    
    return "YES" if solve(0,color,m,n) else "NO"


