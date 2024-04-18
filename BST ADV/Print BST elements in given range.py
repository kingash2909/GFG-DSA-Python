class Solution:
    def solve(self,root, low, high,lst):
        if root==None:
            return
        if low>root.data:
            self.solve(root.right,low,high,lst)
        elif high<root.data:
            self.solve(root.left,low,high,lst)
        else:
            lst.append(root.data)
            self.solve(root.left,low,high,lst)
            self.solve(root.right,low,high,lst)
    
    
    def printNearNodes(self, root, low, high):
        #code here.
        arr = []
        self.solve(root, low, high,arr)
        arr.sort()
        return arr