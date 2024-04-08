class Solution:
    def is_valid(self, A, n, m, mid):
        students = 1
        pages_read = 0
        
        for i in range(n):
            if A[i] > mid:
                return False
            if pages_read + A[i] > mid:
                students += 1
                pages_read = A[i]
            else:
                pages_read += A[i]
            
            if students > m:
                return False
        
        return True
    
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        #code here
        if n < m:
            return -1
        
        low, high = max(A), sum(A)
        result = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            if self.is_valid(A, n, m, mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result
