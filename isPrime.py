class Solution:
    def countPrimes(self, n: int) -> int:
        prime_nums = 0

        def isPrime(i):
            for a in range(2,i-1):
                if i%a == 0:
                    return False
            return True

        for b in range (2,n-1):
            if isPrime(b):
                prime_nums += 1
