
from collections import Counter

class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr,n,k):
        #Your code here
        counter = Counter(arr)
        count = 0
        
        limit = n//k
        
        for i,j in counter.items():
            if j > limit:
                count += 1
        return count