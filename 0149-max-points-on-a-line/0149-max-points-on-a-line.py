class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)
        
        res = 0
        for i in range(len(points)):
            count = 0
            slopes = {}
            slope_found = defaultdict(set)
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x2 - x1 == 0:
                    slope = float('inf')
                else:
                    slope = (y2 - y1) / (x2 - x1)
                if slopes.get(slope):
                    if not ((x1,y1) in slope_found[slope] and (x2,y2) in slope_found[slope]):
                        slopes[slope] += 1
                        count += 1
                else:
                    slopes[slope] = 2
                    count = 2
                slope_found[slope].add((x1,y1))
                slope_found[slope].add((x2,y2))
                # print(slope)
            if len(slopes):
                res = max(res, max(slopes.values()))
            
        # print(slope_found)
        # return max(slopes.values())
        return res