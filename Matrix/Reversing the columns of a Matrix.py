
class Solution:
    
    #Function to reverse the columns of a matrix.
    def reverseCol(self,matrix):
        # code here 
        if not matrix or not matrix[0]:
            return matrix
    
        rows = len(matrix)
        cols = len(matrix[0])
    
        for j in range(cols // 2):
            for i in range(rows):
                # Swap elements of the current column with corresponding elements of the opposite column
                matrix[i][j], matrix[i][cols - 1 - j] = matrix[i][cols - 1 - j], matrix[i][j]
    
        return matrix