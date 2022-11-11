class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)
        res = 0
        for i in range(len(points)):
            slopes = {}
            maxSlope = 0
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x2 - x1 == 0:
                    slope = float('inf')
                else:
                    slope = (y2 - y1) / (x2 - x1)
                if slopes.get(slope):
                    slopes[slope] += 1
                else:
                    slopes[slope] = 2
                maxSlope = max(maxSlope, slopes[slope])
            res = max(res, maxSlope)
        return res