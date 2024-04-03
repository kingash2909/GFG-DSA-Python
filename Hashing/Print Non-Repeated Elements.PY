#User function Template for python3
class Solution:
    
    #Complete this function
    #Function to return non-repeated elements in the array.
    def printNonRepeated(self,arr,n):
        #Your code here
        # Create a dictionary to store the frequency of each element
        frequency_dict = {}
        
        # Iterate through the array and count the frequency of each element
        for num in arr:
            frequency_dict[num] = frequency_dict.get(num, 0) + 1
        
        # Initialize an empty list to collect non-repeated elements
        non_repeated_elements = []
        
        # Iterate through the array and collect non-repeated elements in the order they appear
        for num in arr:
            if frequency_dict[num] == 1:
                non_repeated_elements.append(num)
        
        return non_repeated_elements