
class Solution:
    
    #Function to sort the array according to difference with given number.
    def sortAbs(self,a, n, k):
        #code here
        return sorted(a, key = lambda item: abs(k - item))