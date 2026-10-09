class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        cnt = 0
        intervals.sort()
        r = 1
        for l in range(0,len(intervals)):
            for r in range(l+1 , len(intervals)):
                if intervals[l][1]>=intervals[r][0]:
                    cnt+=1
        
        return cnt