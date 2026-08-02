class DSU:
    def __init__(self,n):
        self.parent = list(range(n+1))
        self.size = [1]*(n+1)
    
    def find(self,node):
        if self.parent[node]!=node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu==pv:
            return False
        if self.size[pu] >= self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
        return True


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        directions  = [[1,0], [-1,0], [0,1] , [0,-1]]
        dsu = DSU(ROWS*COLS)
        def index(r,c):
            return r*COLS+c
        
        islands = 0

        for  r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    islands+=1
                    for dr,dc in directions:
                        nr,nc = r+dr,c+dc
                        if (nr<0 or nc<0 or nr>=ROWS or nc>=COLS or grid[nr][nc] == '0'):
                            continue
                    
                        if dsu.union(index(r,c), index(nr,nc)):
                            islands-=1
        return islands
