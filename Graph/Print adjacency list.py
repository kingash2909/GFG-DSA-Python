
from typing import List


class Solution:
    def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
        # code here 
        ans = [[] for _ in range(V)]
        for i in edges:
            ans[i[0]].append(i[1])
            ans[i[1]].append(i[0])
        return ans
        
