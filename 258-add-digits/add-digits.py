class Solution:
    def addDigits(self, num: int) -> int:
        
        def extract(num):
            sum  = 0
          
            while num>0:
                digit = num%10
                sum = sum+digit

                num = num//10 
            return sum

        while num >= 10:
            num = extract(num)
        
        return num