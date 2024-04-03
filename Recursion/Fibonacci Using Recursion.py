
class Solution:
    def fibonacci(self,n):
        #code here
        if n <= 0:
            return "Invalid input"
        elif n == 1 or n == 2:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)