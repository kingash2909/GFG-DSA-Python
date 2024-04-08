
class Solution:
    
    #Function to find the minimum element in sorted and rotated array.
    def minNumber(self, arr,low,high):
        #Your code here
        # If the array is not rotated, return the first element.
        if arr[low] <= arr[high]:
            return arr[low]
        
        # Perform binary search to find the minimum element.
        while low < high:
            mid = (low + high) // 2
            if arr[mid] <= arr[high]:
                high = mid
            else:
                low = mid + 1
                
        return arr[low]