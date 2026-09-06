class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[0])
        n = len(pairs)
        memo = [[-1] * (n + 1) for _ in range(n)]

        def dp(i,j):
            if i>=n:
                return 0
            if memo[i][j+1]!=-1:
                return memo[i][j+1]
            
            LIS = dp(i+1,j)
            if j==-1 or pairs[j][1]<pairs[i][0]:
                LIS = max(LIS,1+dp(i+1,i))
            
            memo[i][j+1] = LIS
            return LIS
        return dp(0,-1)