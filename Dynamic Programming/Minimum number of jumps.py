
class Solution:
    # Returns minimum number of jumps 
    # to reach arr[n-1] from arr[0] 
    def minimumJumps(self,arr, n):
        #Your code here
        if len(arr)==1:
            return 0
        #print("im in.")
        #print("arr->", arr)
        l=1
        r=arr[0]
        jumps=1
        while r>=l:
            #print("l->",l,"r->",r)
            if l>len(arr)-1:
                #print("check.")
                return jumps-1
            elif l<=len(arr)-1<=r:
                return jumps
            maxi=r
            for i in range(l, r+1):
                if arr[i]+i>maxi:
                    maxi=arr[i]+i
            l=r+1
            r=maxi
            jumps+=1
        return -1
