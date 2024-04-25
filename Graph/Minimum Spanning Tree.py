import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        pq = []
        visit = [False]*V
        res = 0
        heapq.heappush(pq,(0,0))
        while pq:
            wt , u = heapq.heappop(pq)
            if visit[u] == True:
                continue
            visit[u] = True
            res += wt
            for v , weight in adj[u]:
                if visit[v] == False:
                    heapq.heappush(pq,(weight,v))
        return res