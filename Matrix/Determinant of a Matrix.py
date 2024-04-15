
class Solution:
    
    #Function for finding determinant of matrix.
    def determinantOfMatrix(self,matrix,n):
        # code here 

        if n == 1:
            return matrix[0][0]
        
        determinant = 0
        
        # Iterate over the elements in the first row.
        for j in range(n):
            # Calculate the determinant of the submatrix.
            submatrix = [[0] * (n - 1) for _ in range(n - 1)]
            for i in range(1, n):
                for k in range(n - 1):
                    submatrix[i - 1][k] = matrix[i][k if k < j else k + 1]
            # Add the contribution of the current element to the determinant.
            determinant += (-1) ** j * matrix[0][j] * self.determinantOfMatrix(submatrix, n - 1)
        
        return determinant