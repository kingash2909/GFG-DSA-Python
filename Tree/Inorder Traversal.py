

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing the inorder traversal of the tree. 
class Solution:
    def InOrder(self,root):
        # code here

        result = []
        if root is None:
            return result
        
        # Recursively perform inorder traversal on the left subtree
        result.extend(self.InOrder(root.left))
        
        # Append the value of the current node to the result
        result.append(root.data)
        
        # Recursively perform inorder traversal on the right subtree
        result.extend(self.InOrder(root.right))
        
        return result