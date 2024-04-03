
class Solution:
    def leftIndex (self, N, arr, X):
        # code here 
        
        left = 0
        right = N - 1
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == X:
                result = mid
                right = mid - 1  # Look for X in the left half of the array
            elif arr[mid] < X:
                left = mid + 1
            else:
                right = mid - 1
        
        return result