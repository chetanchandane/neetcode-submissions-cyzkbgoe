class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # new interval is completely before current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # new interval is completely after the current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                # newINterval's end time could be overlapping, thus we dont 
                # add the current interval here
            else:
                # means, newInterval is overlapping
                # min of start time, and max of end time
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        # we came past the initial return, means new interval 
        # is at the end of the array.
        res.append(newInterval)
        return res
      