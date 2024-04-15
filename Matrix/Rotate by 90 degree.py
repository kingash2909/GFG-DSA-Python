
class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self,a, n): 
        # code here

        for i in range(n):
            a[i].reverse()
        for i in range(n):
            for j in range(i, n):
                a[i][j], a[j][i] = a[j][i], a[i][j]
                