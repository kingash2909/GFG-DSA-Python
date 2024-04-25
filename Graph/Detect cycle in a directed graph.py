#User function Template for python3
from typing import List

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        # code here
        vs=[False for i in range(V)]
        def pathtraverse(i,s):
            if vs[i]:
                return False
            vs[i]=True
            for x in adj[i]:
                if s[x]:
                    return True
                s[x]=True
                if(pathtraverse(x,s)):
                    return True
                s[x]=False
            return False
        s=[False for i in range(V)]
        for i in range(V):
            if not vs[i]:
                s[i]=True
                if(pathtraverse(i,s)):
                    return True
                s[i]=False
        return False
