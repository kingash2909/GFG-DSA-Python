 
class Solution:
    #Function to find total number of unique paths.
    
    
    def solve(self, m, n):
        prevRow = [1] * (n + 1)
        for i in range(1, m + 1):
            currRow = [0] * (n + 1)
            currRow[0] = 1
            for j in range(1, n + 1):
                currRow[j] = prevRow[j] + currRow[j - 1]
            prevRow = currRow
        return prevRow[n]
        
        
    def NumberOfPaths(self,a, b):
        #code here
        return self.solve(a - 1, b - 1)