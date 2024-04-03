
class Solution:
    #Function to fill the array elements into a hash table 
    #using Linear Probing to handle collisions.
    def linearProbing(self,hashSize, arr, sizeOfArray):
        #Your code here
         # Initialize hash table with -1
        hash_table = [-1] * hashSize
    
        # Iterate through the array and insert elements into the hash table using linear probing
        for num in arr:
            # Calculate the hash value using modulo operation
            hash_value = num % hashSize
    
            # If the calculated index is empty (-1), insert the element
            if hash_table[hash_value] == -1:
                hash_table[hash_value] = num
            else:
                # If the calculated index is occupied, find the next available index using linear probing
                index = (hash_value + 1) % hashSize
                while hash_table[index] != -1:
                    index = (index + 1) % hashSize
    
                # If we find an empty index, insert the element
                hash_table[index] = num
    
        return hash_table