class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        s = set()
        for i in nums:
            s.add(i)
        
        mx,cnt = 0,0
        for num in s:
            if num-1 not in s:
                cnt=1
                x = num

                while x+1 in s:
                    x = x+1
                    cnt=cnt+1
                mx = max(mx,cnt)
        return mx