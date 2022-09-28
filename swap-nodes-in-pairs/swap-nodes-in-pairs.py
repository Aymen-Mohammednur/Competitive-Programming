# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(node):
            swapped = None
            if node.next and node.next.next:
                swapped = swap(node.next.next)
            if node.next:
                temp = node.next
                node.next = swapped
                temp.next = node
                return temp
            return node
        
        if not head:
            return
        temp = swap(head)
        return temp