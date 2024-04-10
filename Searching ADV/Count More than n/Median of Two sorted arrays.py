
class Solution:
    
    #Function to find the median of the two arrays when they get merged.
    def findMedianSortedArrays(self,arr1, n, arr2, n2):
       
        #code here
        merged = []
        i, j = 0, 0
        
        while i < n and j < n2:
            if arr1[i] <= arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        
        while i < n:
            merged.append(arr1[i])
            i += 1
        
        while j < n2:
            merged.append(arr2[j])
            j += 1
        
        total = n + n2
        if total % 2 == 1:
            return merged[total // 2]
        else:
            mid_right = total // 2
            mid_left = mid_right - 1
            return (merged[mid_left] + merged[mid_right]) // 2