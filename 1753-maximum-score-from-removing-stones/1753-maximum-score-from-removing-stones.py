class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        result = 0
        maxHeap = []
        heappush(maxHeap, -a)
        heappush(maxHeap, -b)
        heappush(maxHeap, -c)
        Max1 = -1 * (heappop(maxHeap))
        Max2 = -1 * (heappop(maxHeap))
        while Max1 != 0 and Max2 != 0:
            result += 1
            heappush(maxHeap, -1 * (Max1 - 1))
            heappush(maxHeap, -1 * (Max2 - 1))
            Max1 = -1 * (heappop(maxHeap))
            Max2 = -1 * (heappop(maxHeap))
        return result