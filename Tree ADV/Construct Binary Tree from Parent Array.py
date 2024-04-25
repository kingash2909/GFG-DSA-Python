#User function Template for python3


'''
# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''
class Solution:
    #Function to construct binary tree from parent array.
    def createTree(self,parent,N):
        # your code here
        node_map = {i: Node(i) for i in range(N)}
        head = None
        
        for i in range(N):
            if parent[i] == -1:
                head = node_map[i]
            else:
                parent_node = node_map[parent[i]] 
               
                if parent_node.left is None:
                   parent_node.left = node_map[i]
                else:
                    parent_node.right = node_map[i]
        return head
                
