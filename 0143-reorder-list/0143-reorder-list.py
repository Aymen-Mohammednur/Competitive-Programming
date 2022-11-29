# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return head
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        stack = []
        while slow:
            stack.append(slow)
            slow = slow.next
        while head and stack:
            nxt = head.next
            head.next = stack.pop()
            head.next.next = nxt
            head = head.next.next
        head.next = None