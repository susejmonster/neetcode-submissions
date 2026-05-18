class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        seen = dict()
        key  = 0
        for i in range(0,len(s)):
            if s[i] != " ":
                seen[i] = s[i]
                key = key + 1
            
        
        last_index = next(reversed(seen))
        count  = 0 
        while last_index >= 0 and s[last_index] != " ":
            count += 1
            last_index -= 1

        return count