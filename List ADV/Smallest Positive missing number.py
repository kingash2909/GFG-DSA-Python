
class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        #Your code here
        # Mark the elements which are positive and within the range of the array size.
        marked = [False] * n
        for num in arr:
            if 1 <= num <= n:
                marked[num - 1] = True

        # Find the first unmarked element.
        for i in range(n):
            if not marked[i]:
                return i + 1

        # If all elements are marked, return the size of the array plus 1.
        return n + 1