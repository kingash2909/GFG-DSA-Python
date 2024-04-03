

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#Function to return a list containing the preorder traversal of the tree.
def preorder(root):
   
    # code here

    result = []
    if root is None:
        return result
    
    # Append the value of the current node to the result
    result.append(root.data)
    
    # Recursively perform preorder traversal on the left subtree
    result.extend(preorder(root.left))
    
    # Recursively perform preorder traversal on the right subtree
    result.extend(preorder(root.right))
    
    return result