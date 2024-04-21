
# Tree Node
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    
    #Function to find the least absolute difference between any node
    #value of the BST and the given integer.
    def minDiff(self,root, K):
        # code here
        self.min_diff = float('inf')
        
        # Helper function to find the minimum difference
        def find_min_diff(node, K):
            if node is None:
                return
            
            # Update the minimum difference if the current node's value is closer to K
            if abs(node.data - K) < self.min_diff:
                self.min_diff = abs(node.data - K)
            
            # If K is less than the current node's value, go left
            if K < node.data:
                find_min_diff(node.left, K)
            # If K is more than the current node's value, go right
            elif K > node.data:
                find_min_diff(node.right, K)
            # If K is equal to the current node's value, we've found the closest value
            else:
                self.min_diff = 0
        
        # Start the recursive function
        find_min_diff(root, K)
        
        # Return the minimum difference found
        return self.min_diff