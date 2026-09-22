class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        q = deque()
        q.append(start)
        
        while q:
            idx = q.popleft()
            
            if arr[idx]==0:
                return True
            if arr[idx]<0:
                continue
            dlx = arr[idx]
            arr[idx] = -1

            for i in (idx+dlx,idx - dlx):
                if 0 <= i < len(arr) and arr[i] >= 0:
                    q.append(i)        
        return False