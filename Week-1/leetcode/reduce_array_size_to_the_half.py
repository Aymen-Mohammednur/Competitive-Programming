# LEETCODE 1338
# https://leetcode.com/problems/reduce-array-size-to-the-half/

from typing import Counter, List
import heapq

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        output = 0
        count = len(arr)
        for temp in reversed(sorted(counter.values())):
            count -= temp
            output += 1
            if (count <= len(arr) // 2):
                break
        return output
    
        # counter = Counter(arr)
        # heap = []
        # output = 0
        # count = len(arr)
        # for i in counter:
        #     heapq.heappush(heap, [-counter[i]])
        # while (count > len(arr) // 2):
        #     temp = heapq.heappop(heap)
        #     count += temp
        #     output += 1
        # return output

arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
print(Solution().minSetSize(arr))
