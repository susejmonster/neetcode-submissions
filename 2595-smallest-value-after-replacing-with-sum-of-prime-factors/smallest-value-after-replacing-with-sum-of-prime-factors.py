class Solution:
    def smallestValue(self, n: int) -> int:
        while True:
            temp = n
            sum_factors = 0
            i = 2
            
            # Find prime factors
            while i * i <= temp:
                while temp % i == 0:
                    sum_factors += i
                    temp //= i  # Crucial step: reduce the number
                i += 1
            
            # If there's a prime factor greater than the square root left over
            if temp > 1:
                sum_factors += temp
            
            # If the number hasn't changed (it's either a prime, or 4), we found our answer
            if sum_factors == n:
                return n
            
            # Otherwise, update n and repeat
            n = sum_factors