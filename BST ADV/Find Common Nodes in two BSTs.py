#User function Template for python3


class Solution:
    
    #Function to find the nodes that are common in both BST.
    def inorder(self, root, arr):
        if root is not None:
            self.inorder(root.left, arr)
            arr.append(root.data)
            self.inorder(root.right, arr)
    
    # Function to find the nodes that are common in both BSTs
    def findCommon(self, root1, root2):
        # Lists to store the inorder traversal of the BSTs
        arr1 = []
        arr2 = []
        
        # Perform inorder traversal of both BSTs and store the results
        self.inorder(root1, arr1)
        self.inorder(root2, arr2)
        
        # Use two pointers to find common elements
        i = j = 0
        common = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                i += 1
            elif arr1[i] > arr2[j]:
                j += 1
            else:
                common.append(arr1[i])
                i += 1
                j += 1
        
        return common