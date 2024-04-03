
'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing the postorder traversal of the tree.
def postOrder(root):
    # code here
    result = []
    if root is None:
        return result
    
    # Recursively perform postorder traversal on the left subtree
    result.extend(postOrder(root.left))
    
    # Recursively perform postorder traversal on the right subtree
    result.extend(postOrder(root.right))
    
    # Append the value of the current node to the result
    result.append(root.data)
    
    return result
