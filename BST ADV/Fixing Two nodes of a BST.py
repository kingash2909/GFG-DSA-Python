

#Function to fix a given BST where two nodes are swapped.  
class Solution:
    def correctBST(self, root):
    # code here
        first, second, prev = [None], [None], [None]
        
        # Helper function to perform inorder traversal and find misplaced nodes
        def inorder_traversal(node):
            if not node:
                return
            inorder_traversal(node.left)
            if prev[0] and node.data < prev[0].data:
                if not first[0]:
                    first[0] = prev[0]
                second[0] = node
            prev[0] = node
            inorder_traversal(node.right)
        
        # Start the traversal
        inorder_traversal(root)
        
        # Swap the values of the misplaced nodes
        first[0].data, second[0].data = second[0].data, first[0].data

