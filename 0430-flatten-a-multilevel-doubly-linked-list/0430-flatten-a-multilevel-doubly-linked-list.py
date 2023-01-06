"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr and not curr.child:
            curr = curr.next
        if not curr:
            return head
        nxt = curr.next
        res = self.flatten(curr.child)
        curr.next = res
        res.prev = curr
        curr.child = None
        while curr.next:
            curr = curr.next
        if nxt:
            nxt.prev = curr
            curr.next = nxt
        return head