class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        ans = []
        
        for key,val in freq.items():
          
            if val>len(nums)/3:
                ans.append(key)

        
        return ans