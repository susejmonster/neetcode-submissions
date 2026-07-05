class Solution:

    def __init__(self, nums: List[int]):
        self.d = {}
        for i,v in enumerate(nums):
            self.d.setdefault(v,[]).append(i)

            

    def pick(self, target: int) -> int:
        return random.choice(self.d[target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)