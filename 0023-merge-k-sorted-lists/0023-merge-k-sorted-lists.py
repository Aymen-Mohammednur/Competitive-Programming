# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        heap = []
        for l in lists:
            while l:
                heapq.heappush(heap, l.val)
                l = l.next
        dummy = res
        while heap:
            new = ListNode(heapq.heappop(heap))
            dummy.next = new
            dummy = dummy.next
        return res.next
        