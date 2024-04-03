
"""
@Node Template -
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
"""
def InOrder(root):
    #code here
    result = []
    if root is None:
        return result
    
    # Recursively perform inorder traversal on the left subtree
    result.extend(InOrder(root.left))
    
    # Append the value of the current node to the result
    result.append(root.val)
    
    # Recursively perform inorder traversal on the right subtree
    result.extend(InOrder(root.right))
    
    return result
