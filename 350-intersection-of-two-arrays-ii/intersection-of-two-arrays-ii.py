class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = []
        for i in range(0,len(nums1)):
            ref = nums1[i]
            for j in range(0,len(nums2)):
                if nums2[j]==ref:
                    res.append(nums2[j])
                    del nums2[j]
                    break
        return res