class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def DFS(idx,path):
            if len(path) == len(digits):
                res.append(path)
                return
            for c in map[digits[idx]]:
                DFS(idx+1,path+c)
    
        if digits:
            DFS(0,"")

        return res
