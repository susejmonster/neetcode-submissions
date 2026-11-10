class Solution:
    def countPrimes(self, n: int) -> int:
        cnt = 0
        if n==1:
            return 0
        if n==0:
            return 0

        ##sieve of erastothenes
        primes = [True]*n
        primes[0] = primes[1] = False

        for i in range(2,int(n**0.5)+1):
            if primes[i]:
                for j in range(i*i, n , i):##there is one more extra prime factor after i^2
                    primes[j]=False
        
        return sum(primes)