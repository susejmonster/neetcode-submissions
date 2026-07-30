import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        for x,y in points:
            dis = (x**2) + (y**2)
            h.append([dis,x,y])

        heapq.heapify(h)

        res = []
        while h and k > 0:
            dist, x, y = heapq.heappop(h)
            res.append([x, y])
            k -= 1

        return res 

    