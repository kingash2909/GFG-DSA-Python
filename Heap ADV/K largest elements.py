class Solution:
    #Function to return k largest elements from an array.
    def kLargest(self,li,n,k):
        # code here
        a=[]
        li.sort()
        for i in range(1,k+1):
            a.append(li[-i])
        return a
