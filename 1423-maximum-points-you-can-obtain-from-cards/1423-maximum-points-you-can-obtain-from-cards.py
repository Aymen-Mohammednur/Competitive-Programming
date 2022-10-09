class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l, r = 0, len(cardPoints) - k
        currSum = 0
        for i in range(r, len(cardPoints)):
            currSum += cardPoints[i]
        maxSum = currSum
        while r < len(cardPoints):
            currSum += cardPoints[l]
            currSum -= cardPoints[r]
            maxSum = max(maxSum, currSum)
            l += 1
            r += 1
        return maxSum