class Solution:
    def GCD(self,a,b):
        #code here
        if b == 0:
            return a
        else:
            return self.GCD(b, a % b)