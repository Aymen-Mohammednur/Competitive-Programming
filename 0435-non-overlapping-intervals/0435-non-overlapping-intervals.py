class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        count = 0
        Min = float('-inf')
        for i in range(len(intervals)):
            if intervals[i][0] >= Min:
                Min = intervals[i][1]
            else:
                count += 1
        return count
        
        # result = [intervals[0]]
        # count = 0
        # for i in range(1, len(intervals)):
        #     if intervals[i][0] < result[-1][1]:
        #         count += 1
        #         result[-1][1] = min(result[-1][1], intervals[i][1])
        #     else:
        #         result.append(intervals[i])
        # return count