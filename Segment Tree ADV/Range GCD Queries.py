
'''
// st : segment tree
// n : size of the given array
// l and r : range to find gcd i.e L and R respectively
return: gcd in range
'''

class Solution:
    
    def gcd(self,a,b):
    
        if a<b:
            a,b=b,a
        if b==0:
            return a
        return self.gcd(b,a%b)
        
    #Function to find gcd of given range.
    def findRangeGcd(self,li,rv,arr,st,n):
        return self.frg(st,0,n-1,li,rv,0)
        
    def frg(self,st,ss,se,qs,qe,si):
        
        if ss>qe or se<qs:
            return 0
        if ss>=qs and se<=qe:
             return st[si]
        
        mid = ss+(se-ss)//2
        
        a=self.frg(st,ss,mid,qs,qe,si*2+1)
        b=self.frg(st,mid+1,se,qs,qe,si*2+2)
        
        n=self.gcd(a,b)
        
        return n
        
        
    
        
    #Function to update a value in input array and segment tree.   
    def updateValue(self,li,rv,arr,st,n):
        self.uv(st,li,rv,0,n-1,0)
        
    def uv(self,st,li,rv,ss,se,si):
         #base cases
        if ss>li or se<li:
            return
        if ss==se:
            st[si]=rv
            return
        
        #if the input index is in range of this node then we update
        #the value of the node and its children.
        mid=ss+(se-ss)//2
        
        self.uv(st,li,rv,ss,mid,si*2+1)
        self.uv(st,li,rv,mid+1,se,si*2+2)
        
        st[si]=self.gcd(st[si*2+1],st[si*2+2])

