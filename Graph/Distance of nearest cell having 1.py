#User function Template for python3
from collections import deque
class Solution:

    #Function to find distance of nearest 1 in the grid for each cell.
    def nearest(self, grid):
        #Code here
        
        m = len(grid)
        n = len(grid[0])
        
        seen = set()
        
        q = deque()
        res = [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if(grid[r][c]==1):
                    seen.add((r,c))
                    q.append((r,c,0))
                    
        
        dirs = [(0,-1),(-1,0),(0,1),(1,0)]
        
        while(q):
            
            r,c,dist = q.popleft()
            
            for d in dirs:
                nr = r+d[0]
                nc = c+d[1]
                if((0<=nr<m) and 0<=nc<n):
                    if((nr,nc) not in seen):
                        seen.add((nr,nc))
                        q.append((nr,nc,dist+1))
                        res[nr][nc]=dist+1
        return res
                    