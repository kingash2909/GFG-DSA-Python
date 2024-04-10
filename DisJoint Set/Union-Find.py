

class Solution:
    
    #Function to merge two nodes a and b.
    def union_(self,a,b,par,rank1):
        # code here
        parent_a = self.find(a, par)
        parent_b = self.find(b, par)

        if parent_a == parent_b:
            return

        if rank1[parent_a] < rank1[parent_b]:
            par[parent_a] = parent_b
        elif rank1[parent_a] > rank1[parent_b]:
            par[parent_b] = parent_a
        else:
            par[parent_b] = parent_a
            rank1[parent_a] += 1
            
            
    #Function to check whether 2 nodes are connected or not.
    def isConnected(self,x,y,par,rank1):
        # code here
        return self.find(x, par) == self.find(y, par)
    
    #Function to find the parent of a node.
    def find(self, node, par):
        if par[node] != node:
            par[node] = self.find(par[node], par)
        return par[node]