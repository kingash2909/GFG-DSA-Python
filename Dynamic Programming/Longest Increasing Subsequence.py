
class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        # code here
        if n == 0:
            return 0
        
        # Initialize tail list with the first element of the array
        tail = [a[0]]
        
        # Iterate through each element of the array
        for i in range(1, n):
            # Perform binary search to find the largest index j such that tail[j] < A[i]
            left, right = 0, len(tail) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if tail[mid] < a[i]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            # If such an index j is found, update tail[j + 1] = A[i]
            # Otherwise, append A[i] to tail, creating a new subsequence of length 1
            if left < len(tail):
                tail[left] = a[i]
            else:
                tail.append(a[i])
        
        # Return the length of the tail list
        return len(tail)
