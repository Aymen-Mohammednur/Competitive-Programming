class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -1 * nums[i]
        heapify(nums)
        for _ in range(k - 1):
            heappop(nums)
        return -1 * heappop(nums)