class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        #code here
        arr.sort()
        for i in range(n-1):
            j =i+1
            k =n-1
            while(j<k):
                sum=arr[i]+arr[j]+arr[k]
                if(sum==0):
                    return 1
                elif(sum<0):
                    j +=1
                else:
                    k -=1
                    
        else:
            return 0
    