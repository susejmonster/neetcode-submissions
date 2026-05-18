class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        min = 200
        for s in strs:
            if min > len(s):
                min = len(s)
        prefix = ""
        for i in range(0,min):
            
            for j in range(0,len(strs)):
                if strs[0][i] != strs[j][i]:
                    return prefix    
                
            prefix+=strs[j][i]

        return prefix
