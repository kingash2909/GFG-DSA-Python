
#Function to check if two numbers in the array have sum equal to the given sum.
def sumExists(arr, N, sum):
    ##Your code here
    
     # Sort the array
    arr.sort()
    
    # Initialize two pointers, one at the beginning and one at the end of the array
    left = 0
    right = N - 1
    
    # Iterate until the two pointers meet
    while left < right:
        # Calculate the sum of elements at the current pointers
        current_sum = arr[left] + arr[right]
        
        # If the current sum is equal to the given sum, return 1
        if current_sum == sum:
            return 1
        
        # If the current sum is less than the given sum, move the left pointer forward
        elif current_sum < sum:
            left += 1
        
        # If the current sum is greater than the given sum, move the right pointer backward
        else:
            right -= 1
    
    # If no pair with the given sum is found, return 0
    return 0