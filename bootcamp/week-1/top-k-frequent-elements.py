# LEETCODE 347

from ast import List
from collections import Counter
from heapq import heappop, heappush

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for num in counter:
            heappush(heap, [counter[num], num])
            if len(heap) > k:
                heappop(heap)
        return [heap[i][1] for i in range(len(heap))]