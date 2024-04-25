#User function Template for python3


'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        #Your code here
        res = root.data
        
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            res = max(res, root.data + leftMax + rightMax)
            return root.data + max(leftMax, rightMax)
        
        dfs(root)
        return res   