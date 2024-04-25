from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
        def bfsCycle(d,a,visited):
            q=[]
            q.append([a,-1])
            visited[a]=True
            while q:
                x,y=q.pop(0)
                for i in d[x]:
                    if visited[i]==False:
                        q.append([i,x])
                        visited[i]=True
                    elif i!=y:
                        return True
            return False
            
                    
        d={}
        for i in range(len(adj)):
            d[i]=adj[i]
        visited=[False]*V
        for i in range(V):
           if visited[i]==False and bfsCycle(d,i,visited):
                return True
        return False