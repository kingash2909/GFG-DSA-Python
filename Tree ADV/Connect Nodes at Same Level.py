#User function Template for python3

import sys
sys.setrecursionlimit(50000)
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.nextRight = None
class Solution:
    #Function to connect nodes at same level.
    def connect(self, root):
        
        if not root:
            return
        
        q = []
        q.append(root)
        temp = root
        
        while q:
            l= len(q)
            while l>0:
                node = q[0]
                q.pop(0)
                if l>1:
                    node.nextRight = q[0]
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                l-=1
        return temp
                