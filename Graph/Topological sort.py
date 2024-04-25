from collections import deque


class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here

        vis[node] = 1
        
        for it in adj[node]:
            if vis[it] == 0:
                self.dfs(it, V, vis, adj, stack)
        
        # appending the value to stack
        stack.append(node)
        
    def topoSort(self, V, adj):
        
        indegree = [0]*V
        for i in range(V):
            for it in adj[i]:
                indegree[it] += 1
        
        vis = [0]*V
    
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for it in adj[node]:
                indegree[it] -= 1
                if indegree[it] == 0:
                    q.append(it)
        # print(ans)
        return ans
