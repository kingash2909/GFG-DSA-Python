class Solution:
    
    #Complete this code
    #Function to return the count of non-repeated elements in the array.
    def countNonRepeated(self,arr,n):
        #Your code here
        frequency_dict = {}
        
        # Count the frequency of each element in the array
        for num in arr:
            frequency_dict[num] = frequency_dict.get(num, 0) + 1
        
        # Count the number of non-repeated elements
        count = 0
        for frequency in frequency_dict.values():
            if frequency == 1:
                count += 1
        
        return count
