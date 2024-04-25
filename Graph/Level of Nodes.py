
#User function Template for python3
from collections import deque
class Solution:
    
    #Function to find the level of node X.
    def levelOfX(self, V, adj, X):
        q = deque()
        n = V
        visited = [False]*n
        q.append(0)
        visited[0] = True
        level = 0
        
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == X:
                    return level
                for child in adj[curr]:
                    if not visited[child]:
                        q.append(child)
                        visited[child] = True
                        
            level += 1
            
        return -1
            
        