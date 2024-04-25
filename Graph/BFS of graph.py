
from typing import List
from queue import Queue
from collections import deque

class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        vis = [0] * V
        vis[0] = 1
        q = deque()
        q.append(0)
        bfs = []
        while q:
            node = q.popleft()
            bfs.append(node)
            for it in adj[node]:
                if not vis[it]:
                    vis[it] = 1
                    q.append(it)
        return bfs