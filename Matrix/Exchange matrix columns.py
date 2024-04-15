
class Solution:
    
    #Function to exchange first column of a matrix with its last column.
    def exchangeColumns(self,matrix):
        # code here
        if not matrix or not matrix[0]:
            return matrix
    
        rows = len(matrix)
        cols = len(matrix[0])
    
        for i in range(rows):
            # Swap the elements of the first and last columns
            matrix[i][0], matrix[i][cols - 1] = matrix[i][cols - 1], matrix[i][0]
    
        return matrix