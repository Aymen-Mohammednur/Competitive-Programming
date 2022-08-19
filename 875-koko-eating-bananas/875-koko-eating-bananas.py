class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(k):
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / k)
            return hours
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            if helper(mid) <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left