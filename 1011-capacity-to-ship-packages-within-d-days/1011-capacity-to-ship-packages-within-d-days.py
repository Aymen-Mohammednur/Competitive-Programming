class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def helper(ships):
            day = 0
            currSum = 0
            for i in range(len(weights)):
                if weights[i] > ships:
                    return days + 1
                if currSum + weights[i] <= ships:
                    currSum += weights[i]
                else:
                    day += 1
                    currSum = weights[i]
            if currSum != 0:
                return day + 1
            return day
        left, right = 1, sum(weights)
        while left <= right:
            mid = (left + right) // 2
            if helper(mid) <= days:
                right = mid - 1
            else:
                left = mid + 1
        return left