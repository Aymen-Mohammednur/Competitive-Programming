# LEETCODE 23

# Definition for singly-linked list.
from typing import List, Optional
from heapq import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        curr = dummy
        for linkedList in lists:
            while linkedList:
                heappush(heap, linkedList.val)
                linkedList = linkedList.next
        while heap:
            curr.next = ListNode(heappop(heap))
            curr = curr.next
        return dummy.next