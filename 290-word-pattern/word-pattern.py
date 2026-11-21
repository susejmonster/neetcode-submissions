class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        match = {}
        for i in range(len(pattern)):
            word = words[i]
            letter = pattern[i]

            if letter in match:
                if match[letter] != word:
                    return False
            else:
                ##bijection
                if word in match.values():
                    return False
                match[letter] = word
            
        return True


            