# LEETCODE 692
from ast import List
from collections import Counter
from heapq import *

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # setattr(str, "__lt__", lambda self, other: self.val > other.val)
        counter = Counter(words)
        heap = []
        result = []
        for word in counter:
            heappush(heap, [-counter[word], word])  
        for i in range(k):
            result.append(heappop(heap)[1])
        return result