
class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # your code here
        ans = []
        x = 1
        y = 1
        while n > 0:
             ans.append(x)
             x, y = y, x + y
             n -= 1
        return ans
