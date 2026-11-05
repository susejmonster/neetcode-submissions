class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]

        for i in range(1,len(s)):
            if stack and s[i].swapcase() == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        
        ans = ""
        for i in stack:
            ans+=i
        return ans