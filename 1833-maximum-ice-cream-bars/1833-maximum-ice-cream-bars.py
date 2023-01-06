class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_bars = 0
        costs.sort()
        curr_sum = 0
        for cost in costs:
            if curr_sum + cost > coins:
                break
            curr_sum += cost
            max_bars += 1
        return max_bars