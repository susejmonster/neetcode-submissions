class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        
        outd = [0]*(n+1)
        ind = [0]*(n+1)

        for node,edges in trust:
            outd[node]+=1
            ind[edges]+=1

        for i in range(1,n+1):
            if outd[i] == 0 and ind[i] == n-1:
                return i 
        return -1
                   


