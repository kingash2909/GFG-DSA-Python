'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    
    #Function to return a list of integers denoting the node 
    #values of both the BST in a sorted order.
    def inOrder(self,root,ans):
        if root is None:
            return
        self.inOrder(root.left,ans)
        ans.append(root.data)
        self.inOrder(root.right,ans)
        
    def merge(self, root1, root2):
        ans=[]
        self.inOrder(root1,ans)
        self.inOrder(root2,ans)
        return sorted(ans)
        