
'''
@Node structure -
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
'''
def preOrder(root):
    #code here
    result = []
    if root is None:
        return result
    
    # Append the value of the current node to the result
    result.append(root.val)
    
    # Recursively perform preorder traversal on the left subtree
    result.extend(preOrder(root.left))
    
    # Recursively perform preorder traversal on the right subtree
    result.extend(preOrder(root.right))
    
    return result