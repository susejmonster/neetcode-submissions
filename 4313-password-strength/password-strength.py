class Solution:
    def passwordStrength(self, password: str) -> int:
        distinct_chars = set(password)
        score = 0
        for i in distinct_chars:
            if i.islower():
                score+=1
            elif i.isupper():
                score+=2
            elif i.isdigit():
                score+=3
            elif i in "!@#$":
                score+=5

        return score