

#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):
    
    #your code here
    def isvalid(u,visited,col):
        for v in range(len(graph[u])):
            if graph[u][v] and visited[v] == col:
                return False
        return True
    def rev(u):
        if u == V:
            return True
        for col in range(1,k+1):
            if isvalid(u,visited,col):
                visited[u] = col
                if rev(u+1):
                    return True
                else:
                    visited[u] = 0
        return False
    visited = [0]*V
    return rev(0)