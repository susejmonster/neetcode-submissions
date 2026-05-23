class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        ref = strs[0]
        for i in range(0,len(ref)):
            char = ref[i]
            for j in range(1,len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return ref[:i]
            
        return ref
        
        
