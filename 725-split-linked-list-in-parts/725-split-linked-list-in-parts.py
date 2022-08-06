# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        temp = head
        while temp:
            temp = temp.next
            count += 1
        result = []
        q, rem = count // k, count % k
        curr = head
        prev = None
        for i in range(k):
            result.append(curr)
            for j in range(q):
                if curr:
                    prev = curr
                    curr = curr.next
            if rem and curr:
                prev = curr
                curr = curr.next
                rem -= 1
            if prev:
                prev.next = None
        return result