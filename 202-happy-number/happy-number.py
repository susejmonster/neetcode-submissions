class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        if n == 2:
            return False
        def sqr_sum(n):

            sum = 0
            while n>0:
                digit = n%10
                digit = digit*digit
                sum = sum + digit
                n=n//10
            return sum

        i = 0 
        while n != 1:
            n = sqr_sum(n)
            i += 1
            if i > 2^31:
                return False

        return True