#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        ans = []
        visit = set()
        def dfs(v):
            visit.add(v)
            ans.append(v)
            for adjnode in adj[v]:
                if adjnode not in visit:
                    dfs(adjnode)
        dfs(0)
        return ans
        
