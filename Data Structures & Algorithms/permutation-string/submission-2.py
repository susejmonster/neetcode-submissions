class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        s1_count = {}
        s2_count = {}
        
        # Populate the target frequencies from s1
        # and set up the very first window in s2
        for i in range(len(s1)):
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
            
        if s1_count == s2_count:
            return True
            
        # Slide the window across s2
        l = 0
        for r in range(len(s1), len(s2)):
            # Add the new character on the right side of the window
            s2_count[s2[r]] = s2_count.get(s2[r], 0) + 1
            
            # Remove the old character on the left side of the window
            s2_count[s2[l]] -= 1
            if s2_count[s2[l]] == 0:
                del s2_count[s2[l]]
                
            l += 1
            
            # Check if the current window matches the target
            if s1_count == s2_count:
                return True
                
        return False