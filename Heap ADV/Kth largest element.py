
class Solution:
    #Function to return kth largest element from an array.
    def kthLargest(self,a,n,k):
        
        # code here
        
        b=0
        a.sort()
        for i in range(1,k+1):
            b = a[-k]
        return b
