#User function Template for python3
from collections import deque

'''
@node template - 
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
'''
def levelOrder(root):
    #code here 
    result = []
    if root is None:
        return result
    
    # Create an empty queue for level-order traversal
    queue = deque()
    # Enqueue the root node
    queue.append(root)
    
    while queue:
        # Dequeue the current node
        current_node = queue.popleft()
        # Append the value of the current node to the result
        result.append(current_node.val)
        
        # Enqueue the left child if it exists
        if current_node.left:
            queue.append(current_node.left)
        # Enqueue the right child if it exists
        if current_node.right:
            queue.append(current_node.right)
    
    return result