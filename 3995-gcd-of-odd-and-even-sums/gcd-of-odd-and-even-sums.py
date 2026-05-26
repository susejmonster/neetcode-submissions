class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        
        def GCD(a,b):#larger,smaller
            if b == 0:
                return a
            return GCD(b,a%b)
        
        sumOdd = 0 
        for i in range(0,n):
            sumOdd = sumOdd + i*2 + 1
        sumEven = 0
        for j in range(0,n):
            sumEven = sumEven + j*2
        
        if sumEven > sumOdd:
            return GCD(sumOdd, sumEven)
        elif sumOdd > sumEven:
            return GCD(sumEven, sumOdd)
        else:
            return sumOdd