class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        # for i in range(len(trips)):
        #     curPass = trips[i][0]
        #     for j in range(i):
        #         if trips[j][2] > trips[i][1]:
        #             curPass += trips[j][0]
        #     if curPass > capacity:
        #         return False
        # return True
        min_heap = []  # pair of [end, numPassengers]
        curPass = 0
        for numPass, start, end in trips:
            while min_heap and min_heap[0][0] <= start:
                curPass -= heapq.heappop(min_heap)[1]
            
            curPass += numPass
            if curPass > capacity:
                return False
            heapq.heappush(min_heap, [end, numPass])
        return True
            


