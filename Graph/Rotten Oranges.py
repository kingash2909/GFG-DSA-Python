from collections import deque
class Solution:

    #Function to find minimum time required to rot all oranges. 
    def orangesRotting(self, grid):
        #Code here
        if not grid:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        queue = deque()
        
        # Find all rotten oranges and add their positions to the queue.
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        # If there are no fresh oranges initially, return 0.
        if fresh_count == 0:
            return 0
        
        time = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # BFS traversal to rot oranges.
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_count -= 1
                        queue.append((nx, ny))
            time += 1
            
            # If there are no fresh oranges left, return the time.
            if fresh_count == 0:
                return time
        
        # If there are still fresh oranges left, return -1.
        return -1