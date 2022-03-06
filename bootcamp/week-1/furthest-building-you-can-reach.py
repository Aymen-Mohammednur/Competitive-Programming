# LEETCODE 1642

from typing import List
from heapq import *

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        brickCount = 0
        minHeap = []
        for i in range(len(heights) - 1):
            jump = heights[i + 1] - heights[i]
            if jump > 0:
                if len(minHeap) < ladders:
                    heappush(minHeap, jump)
                else:
                    if minHeap and jump > minHeap[0]:
                        brickCount += heappop(minHeap)
                        heappush(minHeap, jump)
                    else:
                        brickCount += jump
                if brickCount > bricks:
                    return i
        return len(heights) - 1