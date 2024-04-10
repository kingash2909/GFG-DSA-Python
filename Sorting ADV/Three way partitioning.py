
class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
	def threeWayPartition(self, array, a, b):
	    # code here 
        n = len(array)
        low, mid, high = 0, 0, n - 1

        while mid <= high:
            if array[mid] < a:
                array[low], array[mid] = array[mid], array[low]
                low += 1
                mid += 1
            elif array[mid] > b:
                array[mid], array[high] = array[high], array[mid]
                high -= 1
            else:
                mid += 1

        return array