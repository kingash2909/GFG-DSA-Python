
class Solution:
    
    #Function to find two repeated elements.
    def twoRepeated(self, arr , n):
        #Your code here
        count = [0] * (n + 1)
        repeated = []
        
        # Traverse the given array and count the occurrences of each element.
        for x in arr:
            count[x] += 1
        
        # Traverse the count array to find elements occurring twice.
        for i in range(1, n + 1):
            if count[i] == 2:
                repeated.append(i)
        
        return repeated