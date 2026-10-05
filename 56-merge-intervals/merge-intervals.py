class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        merged = []#make res arr
        res = intervals[0]#make new arr ele and append it to first ele of arr

        for i in range(1,len(intervals)):##since thsi starts from 1
            if intervals[i][0]<=res[1]:##greedyh choice due to sorting
                res[1] = max(res[1] , intervals[i][1])#make changes to res as per wish
            else:
                merged.append(res)##append res
                res = intervals[i]##move res poimter along intervals
        
        merged.append(res)##append the last res as well
        return merged