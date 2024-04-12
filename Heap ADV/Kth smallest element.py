class Solution:
    #Function to find the kth smallest element in the array.
    def kthSmallest(self,a,n,k):
       
        b=0
        a.sort()
        for i in range(n):
            b = a[k-1]
        return b
        