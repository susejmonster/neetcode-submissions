class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1 
        for i in range(len(digits)-1 , -1, -1):
            ##for each digit res  =  add 1 add carry
            ##if res is > 9: carry = 1 else carry = 0
            ##digits[i] = res%10
            res = digits[i]+carry
            if res>9:
                carry = 1
            else:
                carry = 0
            digits[i] = res%10
            
        if carry==1:
            return [1]+digits
        return digits