'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        if root is None:
            return 0
        
        # Recursively find the height of the left and right subtrees
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        # Return the maximum height of the left and right subtrees, plus 1 for the current node
        return max(left_height, right_height) + 1
