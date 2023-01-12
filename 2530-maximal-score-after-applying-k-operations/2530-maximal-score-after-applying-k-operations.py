class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, -n)
        score = 0
        while k:
            n = abs(heapq.heappop(heap))
            score += n
            n = math.ceil(n / 3)
            heapq.heappush(heap, -n)
            k -= 1
        return score