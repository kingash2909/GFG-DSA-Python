class Solution:
    def greaterThanX(self,arr,n,x):
        #return required result
        #code here
        count = 0
        for num in arr:
            if num>x:
                count+=1
        return count
