#User function Template for python3


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    
    # code here
    ans = []
    
    # code here
    def traverse(node, row_label):
        
        if not node:
            return 
        
        if len(ans)==row_label:
            ans.append(node.data)
            
            
        traverse(node.left, row_label+1)
        traverse(node.right,row_label+1)
        
    traverse(root, 0)
    return ans
