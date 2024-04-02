class Solution:
    def exactly3Divisors(self,N):
        
        def generate_primes(n):
            primes = [True] * (n + 1)
            primes[0], primes[1] = False, False
            p = 2
            while p * p <= n:
                if primes[p]:
                    for i in range(p * p, n + 1, p):
                        primes[i] = False
                p += 1
            return [i for i in range(2, n + 1) if primes[i]]

        def count_perfect_squares(primes):
            count = 0
            for prime in primes:
                if prime * prime <= N:
                    count += 1
                else:
                    break
            return count
    
        max_prime = int(math.sqrt(N))
        primes = generate_primes(max_prime)
        return count_perfect_squares(primes)
