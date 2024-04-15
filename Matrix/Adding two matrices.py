
class Solution:
 
    #Function to add two matrices.
    def sumMatrix(self,A,B):
        # code here
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            return []  # Matrices have different dimensions, return empty matrix
        
        result = []
        for i in range(len(A)):
            row = []
            for j in range(len(A[0])):
                row.append(A[i][j] + B[i][j])  # Add corresponding elements
            result.append(row)
        
        return result