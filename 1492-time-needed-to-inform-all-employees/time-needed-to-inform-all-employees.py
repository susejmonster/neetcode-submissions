class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        size = n

        sub = collections.defaultdict(list)
        for i,v in enumerate(manager):
            sub[v].append(i)

        self.res = 0
        def dfs(manager,steps):
            self.res = max(self.res,steps)
            for s in sub[manager]:
                dfs(s,steps+informTime[manager])

    
        
        dfs(headID,0)
        return self.res


