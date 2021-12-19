# LEETCODE 347
# https://leetcode.com/problems/top-k-frequent-elements/

from typing import Counter, List
from heapq import heappop, heappush

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        output = []
        for i in counter:
            heappush(heap, [-counter[i], i])
        print(heap)
        for i in range(k):
            mostFrequent = heappop(heap)[1]
            output.append(mostFrequent)
        return output


nums = [1, 1, 1, 2, 2, 3, 3, 3, 3]
k = 2
print(Solution().topKFrequent(nums, k))
