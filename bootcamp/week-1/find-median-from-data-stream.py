# LEETCODE 295

from heapq import *

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == len(self.maxHeap):
            if not self.minHeap:
                heappush(self.minHeap, num)
                return
            if num >= self.minHeap[0] or num >= -1 * self.maxHeap[0]:
                heappush(self.minHeap, num)
            else:
                Max = -1 * heappop(self.maxHeap)
                heappush(self.minHeap, Max)
                heappush(self.maxHeap, -1 * num)
        else:
            if num >= self.minHeap[0]:
                Min = heappop(self.minHeap)
                heappush(self.maxHeap, -1 * Min)
                heappush(self.minHeap, num)
            else:
                heappush(self.maxHeap, -1 * num)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            result = (self.minHeap[0] + (-1 * self.maxHeap[0])) / 2
        else:
            result = self.minHeap[0]
        return result


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()