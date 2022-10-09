class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        for i in range(1, len(cardPoints)):
            cardPoints[i] += cardPoints[i - 1]
        cp = [0] + cardPoints
        maxSum = 0
        currSum = 0
        l, r = 1, len(cardPoints) - k
        while r < len(cp):
            currSum = cp[-1] - cp[r] + cp[l-1]
            maxSum = max(maxSum, currSum)
            l += 1
            r += 1
        return maxSum