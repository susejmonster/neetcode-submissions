class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        visited = [False]*size
        
        def dfs(node,visited):
            visited[node]=True
            for i in range(len(isConnected)):
                if isConnected[node][i] and not visited[i]:
                    dfs(i,visited)


        count = 0 
        for i in range(size):
            if not visited[i]:
                    count = count+1
                    dfs(i,visited)
                    
        
        return count  
        