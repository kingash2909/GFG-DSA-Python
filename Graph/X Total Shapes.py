
class Solution:
    
    #Function to find the number of 'X' total shapes.
	def xShape(self, grid):
		#Code here
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        
        def is_valid(x, y):
            return x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == 'X'
            
        def dfs(x, y):
            visited[x][y] = True
            
            for deltax, deltay in dirs:
                adjx, adjy = x+deltax, y+deltay
                if is_valid(adjx, adjy) and not visited[adjx][adjy]:
                    dfs(adjx, adjy)
            
        shape_count = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 'X' and not visited[x][y]:
                    shape_count += 1
                    dfs(x, y)
                    
        return shape_count