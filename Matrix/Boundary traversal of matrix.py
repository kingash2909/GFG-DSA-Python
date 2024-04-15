
class Solution:
    
    #Function to return list of integers that form the boundary 
    #traversal of the matrix in a clockwise manner.
    def BoundaryTraversal(self,matrix, n, m):
        # code here 
        boundary = []
        
        # Step 1: Extract elements of the first row.
        for i in range(m):
            boundary.append(matrix[0][i])
        
        # Step 2: Extract elements of the last column.
        for i in range(1, n):
            boundary.append(matrix[i][-1])
        
        # Step 3: Extract elements of the last row.
        if n > 1:
            for i in range(m - 2, -1, -1):
                boundary.append(matrix[-1][i])
        
        # Step 4: Extract elements of the first column.
        if m > 1:
            for i in range(n - 2, 0, -1):
                boundary.append(matrix[i][0])
        
        return boundary