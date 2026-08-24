class Solution:
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    def helper(self,i,res,s,sign):
        if i>=len(s) or not s[i].isdigit():
            return res*sign
        
        res = res*10+int(s[i])
        if sign * res <= self.INT_MIN: return self.INT_MIN
        if sign * res >= self.INT_MAX: return self.INT_MAX

        return self.helper(i+1,res,s,sign)

    def myAtoi(self, s: str) -> int:
        #initial cleanup
        res = ""
        i = 0 
        if not s:
            return 0
        sign = 1
        while i < len(s) and s[i]==" ":
            i+=1
        if  i<len(s) and (s[i]=="-" or s[i]=="+"):
            if s[i]=="+":
                sign = 1
            else:
                sign = -1
            i+=1
        
        return self.helper(i,0,s,sign)
        
        