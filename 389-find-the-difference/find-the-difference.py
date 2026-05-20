class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        count  = {}

        for c in t:
            count[c] = count.get(c,0)  + 1
        
        for j in s:
            count[j] -= 1
            if count[j] == 0:
                del count[j]

            
        
        return list(count.keys())[0]