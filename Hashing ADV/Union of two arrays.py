
class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        
        #code here
        s1=[]
        s2=[]
        for i in range(n):
            s1.append(a[i])
        for j in range(m):
            s2.append(b[j])
        f=set(s1).union(set(s2))
        return len(f)