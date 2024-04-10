class Solution:

    def __init__(self):
        self.p = []

    def combine(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x != y:
            self.p[y] = x
            return False
        return True

    def find(self, n):
        if self.p[n] != n:
            self.p[n] = self.find(self.p[n])
        return self.p[n]
        
    #Function to detect cycle using DSU in an undirected graph.
    def detectCycle(self, V, adj):
		#Code here
        self.p = list(range(V))
        for i in range(V):
            for j in adj[i]:
                if i < j:
                    continue
                if self.find(i) == self.find(j):
                    return 1
                self.combine(i, j)
        return 0
