class Solution:
     
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
    def find3Numbers(self,A, n, X):
        # Your Code Here

        A.sort()
        for i in range(0,n-2):
            fixed=A[i]
            new_sum=X-fixed
            j=i+1
            k=n-1
            
            while(j<k):
                if(A[j]+A[k]==new_sum):
                    return True
                elif(A[j]+A[k]>new_sum):
                    k=k-1
                else:
                    j=j+1
        return False