from collections import deque

class Solution:
    def reverse(self, x: int) -> int:
        stack = deque()
        neg = False
        if x < 0:
            x = x*-1
            neg = True
        
        while x>0:
            digit = x%10
            stack.append(digit)
            x=x//10
        res=0
        print(stack)
        n = len(stack)
     
        for i in range(0,n):
            exp = (n-1)-i
            digit = stack.popleft()
            print(digit)
            curr = digit*10**exp
            res+=curr
        
        e = 2**31
        if res < e-1 and res > e*-1:
            if neg:
                return res*-1
            else:
                return res
        else:
            return 0