class Solution:

	#Function to find out minimum steps Knight needs to reach target position.
	def minStepToReachTarget(self, KnightPos, TargetPos, N):
		#Code here
        chessboard = [[0] * N for _ in range(N)]

        # Initialize the queue for BFS
        q = [(KnightPos[0] - 1, KnightPos[1] - 1)]
        chessboard[KnightPos[0] - 1][KnightPos[1] - 1] = 1

        # Possible moves for the Knight
        moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

        # Perform BFS
        while q:
            x, y = q.pop(0)

            # Check if the Knight has reached the target position
            if x == TargetPos[0] - 1 and y == TargetPos[1] - 1:
                return chessboard[x][y] - 1

            # Explore all possible moves
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and chessboard[nx][ny] == 0:
                    q.append((nx, ny))
                    chessboard[nx][ny] = chessboard[x][y] + 1

        # If the target position is not reachable
        return -1

