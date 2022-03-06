# LEETCODE 378

from typing import List
from heapq import *

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        for i in range(min(k, len(matrix))):
            heappush(minHeap, (matrix[i][0], (i,0)))
        while k > 1:
            Min = heappop(minHeap)
            row = Min[1][0]
            column = Min[1][1]
            k -= 1
            if column + 1 < len(matrix):
                heappush(minHeap, (matrix[row][column+1], (row, column+1)))
        return heappop(minHeap)[0]