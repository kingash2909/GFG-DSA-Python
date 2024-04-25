

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

'''

class Solution:
    def concatenate(self, leftList, rightList):
        
        #if either of the lists is empty, we return the other list.
        if(leftList is None):
            return rightList
        if(rightList is None):
            return leftList
            
        #storing the last node of left list.
        leftLast=leftList.left
        #storing the last node of right list.
        rightLast=rightList.left
        
        #connecting the last node of Left list with the first 
        #node of the right list.
        leftLast.right=rightList
        rightList.left=leftLast
        
        #left of first node points to the last node in the list.
        leftList.left=rightLast
        
        #right of last node refers to the first node of the list.
        rightLast.right=leftList
        
        return leftList
        
    #Function to convert binary tree into circular doubly linked list.    
    def bTreeToClist(self, root):
        if root is None:
            return None
        
        #calling the function for left and right subtrees recursively.
        left=self.bTreeToClist(root.left)
        right=self.bTreeToClist(root.right)
        
        #making a circular linked list of single node. To do so, we make the  
        #right and left pointers of this node point to itself.
        root.left=root.right=root
        
        #firstly, concatenating the left list with the list with 
        #single node i.e. current node. 
        #then concatenating the returned list with the right list.
        return self.concatenate(self.concatenate(left,root),right)