#User function Template for python3



class Solution:
    
    #Function to return the diameter of a Binary Tree.
    def diameter(self,root):
        # Code here
        if not root:
            return 
        
        d = [0]
        
        self.h(root, d)
            
        return d[0] +1
        
    def h(self, root, d):
        if not root:
            return 0
            
        lh = self.h(root.left, d)
        rh = self.h(root.right, d)
        
        d[0] = max(lh+rh, d[0])
            
        return max(lh, rh)+1