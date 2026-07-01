class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        n = len(arr)
        idx = 0 
        for i in range(1,n):#linear search
            if abs(arr[idx] - x) > abs(arr[i] - x):
                idx = i
        
        res = [arr[idx]]
        l,r = idx-1,idx+1

        while len(res)<k:
            if l >= 0 and r < n:
                if abs(x-arr[l]) <= abs(x - arr[r]):
                    res.append(arr[l])
                    l-=1
                else:
                    res.append(arr[r])
                    r+=1
            elif l>=0:
                res.append(arr[l])
                l-=1
            elif r<n:
                res.append(arr[r])
                r+=1
        return sorted(res)
        