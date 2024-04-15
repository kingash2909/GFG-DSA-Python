

class Solution:
    
    #Function to return sum of upper and lower triangles of a matrix.
    def sumTriangles(self,matrix, n):
        # code here 
        row = len(matrix)
        col = len(matrix[0])
        
        sum_of_upper_triangle = 0
        sum_of_lower_triangle = 0
        
        for i in range(row):
            for j in range(i, col):
                sum_of_upper_triangle += matrix[i][j]
        
        for i in range(row):
            for j in range(i+1):
                sum_of_lower_triangle += matrix[i][j]
        
        return (sum_of_upper_triangle, sum_of_lower_triangle)