class Solution:
    def findLHS(self, nums: list[int]) -> int:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        mx = 0
        for x in freq:
            if x + 1 in freq:
                mx = max(mx, freq[x] + freq[x + 1])

        return mx

            