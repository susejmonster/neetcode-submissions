class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        arr.sort(key = lambda num: abs(num-x))
        res = arr[:k]
        res.sort()       
        return res