
'''
@Node Template - 
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
'''
def postOrder(root):
    #code here
    result = []
    if root is None:
        return result
    
    # Recursively perform postorder traversal on the left subtree
    if root.left:
        result.extend(postOrder(root.left))
    
    # Recursively perform postorder traversal on the right subtree
    if root.right:
        result.extend(postOrder(root.right))
    
    # Append the value of the current node to the result
    result.append(root.val)
    
    return result
    