class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        j = 0
        n = len(tokens)
        
        res = []
        while j<n:
            if tokens[j] == "+":
                digit1 = res.pop()
                digit2 = res.pop()
                res.append(digit1 + digit2)
            elif tokens[j] == "*":
                digit1 = res.pop()
                digit2 = res.pop()
                res.append(digit1 * digit2) 
            elif tokens[j] == "-":
                digit1 = res.pop()
                digit2 = res.pop()
                res.append(digit2 - digit1)
            elif tokens[j] == "/" :
                digit1 = res.pop()
                digit2 = res.pop()
                res.append(int(float(digit2) / digit1))
            else:
                res.append(int(tokens[j]))
            j+=1
        return res[0]


