class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        c=1
        mx=1
        j=1
        i=0
        while(j<len(arr)):
            if dep[i]>=arr[j]:
                c+=1
                mx=max(mx,c)
                j+=1
            else:
                i+=1
                c-=1
        return mx