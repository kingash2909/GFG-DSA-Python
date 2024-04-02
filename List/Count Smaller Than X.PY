
class Solution:
    def smallerThanX(self,arr,n,x):
        #return required ans
        #code here
        count = 0
        for num in arr:
            if num < x:
                count += 1
        return count