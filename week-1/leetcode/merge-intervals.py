# LEETCODE 56
# https://leetcode.com/problems/merge-intervals/

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals.sort()
        output.append(intervals[0])
        for j in range(len(intervals)):                
            if (output[-1][1] >= intervals[j][0]):
                output[-1][1] = max(output[-1][-1], intervals[j][-1])
            else:
                output.append(intervals[j])
        return output

lst = [[1, 4], [0, 0]]
print(Solution().merge(lst))
