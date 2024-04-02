class Solution:
    def digitsInFactorial(self,N):
        # code here
        res=1

        for x in range(2,N+1):
        
          res=res+math.log10(x)
        
        return math.floor(res)