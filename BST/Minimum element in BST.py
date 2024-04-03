
"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""

class Solution:
    #Function to find the minimum element in the given BST.
    def minValue(self, root):
        ##Your code here
        # Check if the tree is empty
        if root is None:
            return None
        
        # Traverse towards the leftmost node
        while root.left is not None:
            root = root.left
        
        # The leftmost node contains the minimum value
        return root.data   