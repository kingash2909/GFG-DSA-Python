
class Solution:
    #Function to rearrange an array so that arr[i] becomes arr[arr[i]]
    #with O(1) extra space.
    def arrange(self,arr, n): 
        #Your code here
        # Traverse the array and store the original values of arr[i] at corresponding indices
        for i in range(n):
            arr[i] += (arr[arr[i]] % n) * n
        
        # Traverse the array again and set each element arr[i] to its transformed value arr[arr[i]]
        for i in range(n):
            arr[i] //= n
    