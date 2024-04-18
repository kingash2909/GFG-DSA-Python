
# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        
        # code here
        dict={}
        q=[(root,0)]
        while(q):
            nod,level=q.pop(0)
            if level not in dict:
                dict[level]=nod.data
            if nod.left:
                q.append((nod.left,level-1))
            if nod.right:
                q.append((nod.right,level+1))
        
        sorted_hds = sorted(dict.keys())

        # Extract top view nodes in left-to-right order
        result = [dict[hd] for hd in sorted_hds]
        # code here
        return result