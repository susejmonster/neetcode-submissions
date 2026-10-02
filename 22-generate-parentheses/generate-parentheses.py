class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n==1:
            return ["()"]
        n-=1
        res = []

        def f(l,r,s):
            if not l and not r:
                res.append(s+")")
                return

            if l>0:
                f(l-1,r,s+"(")
            if r>=l:
                f(l,r-1 , s+")")

        f(n,n,"(")
        return res

 