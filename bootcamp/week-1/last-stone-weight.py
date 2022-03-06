# LEETCODE 1046

from typing import List
from heapq import *

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
        heapify(stones)
        while len(stones) > 1:
            y = -1 * (heappop(stones))
            x = -1 * (heappop(stones))
            if x != y:
                heappush(stones, -1 * (y - x))
        return -1 * stones[0] if stones else 0