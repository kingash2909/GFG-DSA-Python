
class Solution:
	def ShortestDistance(self, matrix):
		# Code here
        if i==m-1 and j==m-1:
            return True
        
        if a[i][j]!=0:
            for k in range(1,a[i][j]+1):
                if j+k<m:
                    r[i][j+k]=1
                    if self.maze(a,m,r,i,j+k):return True
                    r[i][j+k]=0
                if i+k<m:
                    r[i+k][j]=1
                    if self.maze(a,m,r,i+k,j):return True
                    r[i+k][j]=0
        return False