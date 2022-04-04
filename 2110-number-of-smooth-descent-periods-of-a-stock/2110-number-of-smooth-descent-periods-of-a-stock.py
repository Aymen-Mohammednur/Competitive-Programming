class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = 1
        output = 0
        for i in range(len(prices) - 1):
            if prices[i] - prices[i + 1]  == 1:
                count += 1
            else:
                output += (count * (count + 1)) // 2
                count = 1
        if count >= 1:
            output += (count * (count + 1)) // 2
        return output