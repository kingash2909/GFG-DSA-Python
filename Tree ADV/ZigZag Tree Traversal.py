
'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        # Your code here

        result = []
        if not root:
            return result
        
        q = deque()
        q.append(root)
        leftToRight = True
        while q:
            size = len(q)
            row_values = []
            for _ in range(size):
                node = q.popleft()
                row_values.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not leftToRight:
                row_values.reverse()  # Reverse the values for alternate rows
            result.extend(row_values)
            leftToRight = not leftToRight
        return result