class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        color = [0]*len(graph)
        q = deque()
        q.append(graph[0])
        
        for node in range(len(graph)):
            if color[node]!=0:
                continue

            q=deque()
            q.append(node)
            color[node]=1
            while q:
                cur = q.popleft()

                for ne in graph[cur]:
                    if color[ne]==0:
                        color[ne] = -color[cur]
                        q.append(ne)
                    elif color[ne]!=-color[cur]:
                        return False
        return True