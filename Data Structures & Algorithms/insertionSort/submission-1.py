# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        res = []
        for j in range(n):
            i = j - 1 
            while i >= 0 and pairs[i].key > pairs[i+1].key:
                tmp = pairs[i]
                pairs[i] = pairs[i+1]
                pairs[i+1] = tmp
                i-=1
            res.append(pairs[:])
        return res