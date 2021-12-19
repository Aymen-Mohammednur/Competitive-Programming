# LEETCODE 973
# https://leetcode.com/problems/k-closest-points-to-origin/

import math
import heapq

class Solution:
    def helper(self, p1):
        temp1 = math.sqrt((p1[0]**2) + (p1[1]**2))
        return temp1

    def kClosest(self, points, k):
        heap = []
        for i in range(len(points)):
            dist = self.helper(points[i])
            heapq.heappush(heap, [dist, points[i]])
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result


a = ["1", "2", "12", "21"]
print(a[-3])
