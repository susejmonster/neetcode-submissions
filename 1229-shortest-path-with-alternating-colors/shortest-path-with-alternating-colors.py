class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = 1
        blue = 2
        prev = 0
    #remake adjacecny list
        adj = [[] for _ in range(n)]
    
    #ans to store the distances to each node
        for u,v in redEdges:
            adj[u].append((v,red))  
        for u,v in blueEdges:
            adj[u].append((v,blue))
    
    #run level by level bfs(bfs using state)
        q = deque([(0,prev,0)])
        ans=[-1]*n
        step = 0
        while q:
            u,prevcolor,step = q.popleft()

        #get no of steps into answer array
            if ans[u] == -1:
                ans[u] = step
        ##bcs to stop bfs: for nei in adj list ele
            for i,(v,edgecolor) in enumerate(adj[u]):
                if v==-1 or edgecolor == prevcolor:
                    continue
            
                q.append((v,edgecolor,step+1))
                adj[u][i] = (-1,edgecolor)
           

        return ans
        
    