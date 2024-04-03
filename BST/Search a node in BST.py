
class BST:
    
    #Function to search a node in BST.
    def search(self, node, x):
        #code here

        # If the node is None or the value matches X, return the node
        if node is None or node.data == x:
            return node
        
        # If X is less than the current node's value, search in the left subtree
        if x < node.data:
            return self.search(node.left, x)
        
        # If X is greater than the current node's value, search in the right subtree
        return self.search(node.right, x)