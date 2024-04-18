
class Solution:
    #Function to find the nth fibonacci number using bottom-up approach.
    def findNthFibonacci(self,number):
        # Your Code Here
        if number <= 0:
            return 0
        elif number == 1 or number == 2:
            return 1
        
        # Initialize an array to store Fibonacci numbers
        fib = [0] * (number + 1)
        fib[1] = 1  # First Fibonacci number
        fib[2] = 1  # Second Fibonacci number
        
        # Compute Fibonacci numbers bottom-up
        for i in range(3, number + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        
        # Return the nth Fibonacci number
        return fib[number]
