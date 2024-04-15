
class Solution:
    
    #Function to return list of integers visited in snake pattern in matrix.
    def snakePattern(self, matrix): 
       # code here 
        m = len(matrix)
        n = len(matrix[0])
        l = []
        for i in range(m):
            if i%2==0:
                for j in range(n):
                    l.append(matrix[i][j])
            else:
                for j in range(n-1,-1,-1):
                    l.append(matrix[i][j])
        return l