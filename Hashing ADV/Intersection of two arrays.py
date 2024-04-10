#User function Template for python3

#Function to return the count of the number of elements in
#the intersection of two arrays.
class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        #return: expected length of the intersection array.
        
        #code here
        s1=[]
        s2=[]
        for i in range(n):
            s1.append(a[i])
        for j in range(m):
            s2.append(b[j])
        f=set(s1).intersection(set(s2))
        return len(f)