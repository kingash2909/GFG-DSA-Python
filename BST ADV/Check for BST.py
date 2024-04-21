
class Solution:
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root, left=float('-inf'), right=float('inf')):
        # Base case: empty tree is a BST
        if root is None:
            return True
        
        # If this node violates the min/max constraint, return False
        if root.data <= left or root.data >= right:
            return False
        
        # Otherwise, check the subtrees recursively, tightening the min/max constraints
        return (self.isBST(root.left, left, root.data) and
                self.isBST(root.right, root.data, right))


