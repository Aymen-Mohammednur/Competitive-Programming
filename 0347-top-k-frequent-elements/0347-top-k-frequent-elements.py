class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for n in counter:
            heapq.heappush(heap, [-1 * counter[n], n])
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res