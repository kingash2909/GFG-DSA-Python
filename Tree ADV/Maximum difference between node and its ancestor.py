#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return the maximum difference between any node and its ancestor.
#Back-end complete function Template for Python 3

_MIN = -2147483648
_MAX = 2147483648

#Function to find the maximum difference.
def maxDiffUtil(t, res):
    
    #returning Maximum int value if node is null.
    if (t == None):
        return _MAX, res
  
    #if there are no child nodes then we just return data at current node.
    if (t.left == None and t.right == None): 
        return t.data, res 
  
    #recursively calling for left and right subtrees and 
    #choosing their minimum.
    a, res = maxDiffUtil(t.left, res) 
    b, res = maxDiffUtil(t.right, res) 
    val = min(a, b) 
  
    #updating res if (node value - min value from subtrees) is bigger than res.
    res = max(res, t.data - val) 
      
    #returning minimum value got so far.
    return min(val, t.data), res


#Function to return the maximum difference between any node and its ancestor.
def maxDiff(root):
    
    res = _MIN 
    x, res = maxDiffUtil(root, res) 
    #returning the result.
    return res 

