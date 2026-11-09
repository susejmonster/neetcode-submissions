class Solution:
    def distinctPrimeFactors(self, nums: list[int]) -> int:
        
        fnd_primes=set()

        ##for each num in nums, check if it is a prime and if it is, add it to the set
        for num in nums:
            d = 2
            while d*d <= num:
                while num%d==0:
                    fnd_primes.add(d)
                    num = num//d
                d+=1
        ##base case, some part of the original number is left, then automatically it is a prime itself. 
            if num>1:
                fnd_primes.add(num)
        
        return len(fnd_primes)                

        