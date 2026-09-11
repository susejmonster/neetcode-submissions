class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        s = set(bank)
        if endGene not in s and startGene!=endGene:
            return -1
        
        q = deque([(startGene,0)])
        visited = {startGene}#vsiited

        while q:
            g,d = q.popleft()
            if g==endGene:
                return d
            for i in range(8):
                for c in 'ACGT':
                    if g[i]!=c:
                        n=g[:i]+c+g[i+1:]#putting string within string(changing a letter)
                        if n in s and n not in visited:
                            visited.add(n)#visited
                            q.append((n,d+1))
        return -1