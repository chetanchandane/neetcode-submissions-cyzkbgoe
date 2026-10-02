class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # 1. newInterval is completely BEFORE the current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
                
            # 2. newInterval is completely AFTER the current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                
            # 3. OVERLAP: Update newInterval, but DO NOT append it yet!
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
                
        # If we get through the whole loop without returning, 
        # it means newInterval belongs at the very end.
        res.append(newInterval)
        return res