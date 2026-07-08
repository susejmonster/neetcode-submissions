class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)} #make empty array and place each course a and b in it
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visiting = set() #tracking current "[path]"

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True
            
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visiting.remove(crs)
            preMap[crs] = []#memoization step:clearing memo
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
