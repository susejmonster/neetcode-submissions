"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        

        for i in range(0,len(intervals)):
            for j in range(i+1,len(intervals)):
                if min(intervals[j].end,intervals[i].end) > max(intervals[j].start,intervals[i].start):
                    return False

        return True