class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @cache
        def dp(l, r, consecutive):
            if l > r:
                return 0
            while l + 1 <= r and boxes[l] == boxes[l + 1]:
                l += 1
                consecutive += 1
            points = (consecutive + 1) ** 2 + dp(l + 1, r, 0)
            for i in range(l + 1, r + 1):
                if boxes[i] == boxes[l]:
                    points = max(points, dp(i, r, consecutive + 1) + dp(l + 1, i - 1, 0))
            return points
        return dp(0, len(boxes) - 1, 0)