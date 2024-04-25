
class Solution:
    
    #Function to find whether a path exists from the source to destination.
	def is_Possible(self, grid):
		#Code here
        n = len(grid)
        # Directions for up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Find the source and destination coordinates
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    source = (i, j)
                elif grid[i][j] == 2:
                    destination = (i, j)
        
        # Perform DFS to find the path from source to destination
        def dfs(x, y):
            # If out of bounds or on a wall, return False
            if x < 0 or x >= n or y < 0 or y >= n or grid[x][y] == 0:
                return False
            # If destination is reached, return True
            if (x, y) == destination:
                return True
            # Mark the cell as visited
            grid[x][y] = 0
            # Explore all possible directions
            for dx, dy in directions:
                if dfs(x + dx, y + dy):
                    return True
            # Backtrack and unmark the cell
            grid[x][y] = 3
            return False
        
        # Start DFS from the source cell
        return dfs(source[0], source[1])