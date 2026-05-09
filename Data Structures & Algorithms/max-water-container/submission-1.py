class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amnt = heights[0]*1
        max_bar = heights[0]
        for i in range(0,len(heights)):
            if heights[i] >= max_bar:
                max_bar =  heights[i]

                for j in range(i+1,len(heights)):
                    tmp = min(heights[i], heights[j]) * (j-i)
                    if tmp > max_amnt:
                        max_amnt = tmp
        return max_amnt