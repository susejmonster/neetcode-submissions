class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []#result list
        A_st = newInterval[0]
        A_en = newInterval[1]
        for i in range(0,len(intervals)):
            if A_en < intervals[i][0]:#case1
                res.append(newInterval)
                return res+intervals[i:]
            elif A_st > intervals[i][1]:#case2
                res.append(intervals[i])
            else:#case3
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]

        res.append(newInterval)
        return res