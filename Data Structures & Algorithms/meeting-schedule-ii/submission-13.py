"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[Interval]]) -> int:
        # if len(intervals)==0:
        #     return 0
        # free = [] #heap
        # # intervals = [[x, y] for x, y in intervals]
        # intervals.sort(key=lambda x:x.start)
        # heapq.heappush(free, intervals[0].end)
        # for i in intervals[1:]:
        #     if free[0] <= i.start:
        #         heapq.heappop(free)
        #     heapq.heappush(free, i.end)
        # return len(free)
        if not intervals:
            return 0

        start = sorted([x.start for x in intervals])
        end = sorted([interval.end for interval in intervals])
        s = e = 0
        count = 0
        res = 0
        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                # means a meeting just ended, free up room
                count -= 1
                e += 1
            res = max(res, count)
        return res
