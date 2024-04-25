#User function Template for python3

'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        # Code here
        def post(root):
            if root is None:
                return
            post(root.left)
            post(root.right)
            root.left,root.right=root.right,root.left
        post(root)