##Complete this function
#Function to check if there is a pair with the given sum in the array.
def sumExists(arr, N, sum):
    #Your code here
        # Create an empty set to store elements
    num_set = set()

    # Iterate through the array
    for num in arr:
        # Check if the difference between the sum and the current element is in the set
        if sum - num in num_set:
            return 1  # Pair with the given sum exists
        # Add the current element to the set
        num_set.add(num)

    # No pair with the given sum exists
    return 0