class Solution:
    def checkValidString(self, s: str) -> bool:
        
        n = len(s)
        memo = {}
        def f(i,balance):
            if i==n:
                return balance==0
            if balance<0:
                return False
            if (i,balance) in memo:
                return memo[(i,balance)]
            if s[i]=="(":
                ans = f(i+1,balance+1)
            elif s[i]==")":
                ans = f(i+1,balance-1)
            else:
                ans = f(i+1,balance) or f(i+1,balance+1) or f(i+1,balance-1)
            memo[(i,balance)]=ans
            return ans
        return f(0,0)

                    