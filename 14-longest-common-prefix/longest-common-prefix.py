class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        stack = strs[0]

        for i in range(1,len(strs)):
            prefix = ""
            for j in range(0,len(stack)):
                if  j < len(strs[i]) and strs[i][j] == stack[j]:
                    prefix+=strs[i][j]
                else:
                    break
            stack = prefix
        
        return stack
