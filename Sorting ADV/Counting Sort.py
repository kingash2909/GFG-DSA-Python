
class Solution:
    #Function to arrange all letters of a string in lexicographical 
    #order using Counting Sort.
    def countSort(self,arr):
        # code here

        # Create a list to store the count of each character.
        count = [0] * 26  # Assuming only lowercase English letters are present

        # Count the occurrences of each character.
        for char in arr:
            count[ord(char) - ord('a')] += 1

        # Create an empty string to store the sorted result.
        sorted_str = ''

        # Iterate through the count array and append characters
        # to the sorted string in lexicographical order.
        for i in range(26):
            sorted_str += chr(ord('a') + i) * count[i]

        return sorted_str