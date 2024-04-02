class Solution:
    def isPrime(self,N):
        # code here
        if N <= 1:
            return False
        if N <= 3:
            return True
        if N % 2 == 0 or N % 3 == 0:
            return False
        sqrt_N = int(math.sqrt(N))
        for i in range(5, sqrt_N + 1, 6):
            if N % i == 0 or N % (i + 2) == 0:
                return False
        return True  