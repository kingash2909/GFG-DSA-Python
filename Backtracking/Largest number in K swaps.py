
class Solution:
    
    #Function to find the largest number after k swaps.
    def findMaximumNum(self,s,k):
        #code here
        l=list(s)
        maxi=[int(s)]
        n=len(l)
        def swap(x,y,var):
            xx=int(l[x]);yy=int(l[y])
            xval=(10**(n-1-x))
            yval=(10**(n-1-y))
            var-=(xval*xx+yval*yy)
            var+=(xval*yy+yval*xx)
            return var
            
            
        def solve(i,k,curr):
            
            maxi[0]=max(maxi[0],curr)
            if k==0 or i==n:
                return
            
            curr_max=i
            for j in range(i,n):
                if l[j]>l[curr_max]:
                    curr_max=j
            
            if curr_max==i:
                solve(i+1,k,curr)
                    
            for j in range(i,n):
                if l[j]==l[curr_max]:
                    curr=swap(i,j,curr)
                    l[j],l[i]=l[i],l[j]
                    solve(i+1,k-1,curr)
                    curr=swap(i,j,curr)
                    l[j],l[i]=l[i],l[j]
                    
        solve(0,k,int(s))
        return maxi[0]