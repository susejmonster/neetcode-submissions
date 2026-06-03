class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i,a in enumerate(nums):
            if a>0:
                break##sorted array, so all positive after this. never 0
            if i>0 and a == nums[i-1]:
                continue##skip duplicates
            
            l = i+1
            r = len(nums)-1
            while l<r:
                sum = a + nums[l]+nums[r]
                if sum>0:
                    r-=1
                elif sum<0:
                    l+=1
                else:
                    triplets.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1##skip duplicated inside window,edge case

        return triplets
                
