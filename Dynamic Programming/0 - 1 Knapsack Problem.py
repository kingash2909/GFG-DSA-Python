
class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        dp={}
        def solve(cap,wt,val,n):
            cwt=wt[n-1]
            cv=val[n-1]
            if n==0 or cap==0:
                return 0
            elif (cap,n) in dp:
                return dp[(cap,n)]
                
            else:
                if cap<cwt:
                    c=solve(cap,wt,val,n-1)
                else:
                    c1=cv+solve(cap-cwt,wt,val,n-1)
                    c2=solve(cap,wt,val,n-1)
                    c=max(c1,c2)
                dp[(cap,n)]=c
                return c
        
        return solve(W,wt,val,n)