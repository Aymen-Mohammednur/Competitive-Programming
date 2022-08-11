class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        maxHeap = []
        for i in range(k):
            heappush(maxHeap, [-1 * nums[i], i])
        left, right = 1, k
        result = [-1 * maxHeap[0][0]]
        while right < len(nums):
            heappush(maxHeap, [-1 * nums[right], right])
            while maxHeap[0][1] < left:
                heappop(maxHeap)
            result.append(-1 * maxHeap[0][0])            
            left += 1
            right += 1
        return result