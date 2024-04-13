class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        candidate = 0
        
        for i in range(n):
            if i != candidate and M[candidate][i]:
                candidate = i
        
        for i in range(n):
            if i != candidate and (M[candidate][i] == 1 or M[i][candidate] == 0):
                return -1
            
        return candidate