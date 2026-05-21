class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        arr = [-s for s in stones]
        heapq.heapify(arr)

        while len(arr)>1:
            i = heapq.heappop(arr)
            j = heapq.heappop(arr)
            if j > i:
                heapq.heappush(arr,i-j)
        
        arr.append(0)

        return abs(arr[0])