class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        num = []        
        while x > 0:
            digit = x%10
            num.append(digit)
            x = x//10

        l = 0
        r = len(num) - 1

        while l < r:
            if num[l] != num[r]:
                return False
            
            l += 1
            r -= 1
        return True