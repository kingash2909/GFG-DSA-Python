#User function Template for python3

'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

class Solution:
    #Function to return the lowest common ancestor in a Binary Tree.
    def lca(self,root, n1, n2):
        # Code here
        def bst(root):
            if root == None:
                return None
            if root.data == n1 or root.data == n2:
                return root
            l = bst(root.left)
            r = bst(root.right)
            if l == None:
                return r
            if r == None:
                return l
            return root
        return bst(root)

