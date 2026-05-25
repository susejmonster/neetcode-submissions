class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        count = {}

        for i in nums:
            count[i] = count.get(i,0)+1
        
        arr = []
        for i in count:
            j = 1
            while j<=k and j<=count[i]:
                arr.append(i)
                j+=1
        arr.sort()
        return arr