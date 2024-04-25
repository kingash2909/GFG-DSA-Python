#User function Template for python3

'''
@input - 
node - root node of given tree
k = distance of nodes required 

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    #Function to return count of nodes at a given distance from leaf nodes.
    def printKDistantfromLeafUtil(self, node, visited, pathLen, k):
        global c
        
        #base case
        if node == None:
            return
    
        visited[pathLen]=0
        pathLen+=1
        
        #if itâ€™s a leaf node, we increment the count but only if the 
        #same ancestor at distance k is not already counted.
        if(node.left==None and node.right==None and pathLen-k-1>=0 and visited[pathLen-k-1]==0):
            c+=1
            #setting the ancestor as visited so that we won't count it again.
            visited[pathLen-k-1]=1
            return
    
        #if the current node is not a leaf node then we call the function 
        #recursively for left and right subtrees
        self.printKDistantfromLeafUtil(node.left, visited, pathLen, k)
        self.printKDistantfromLeafUtil(node.right, visited, pathLen, k)
    
    #Function to return count of nodes at a given distance from leaf nodes.
    def printKDistantfromLeaf(self, node, k):
        global c
        c=0
        visited = [0]*MAX_HEIGHT
        self.printKDistantfromLeafUtil(node, visited, 0, k)
        #returning the count.
        return c

