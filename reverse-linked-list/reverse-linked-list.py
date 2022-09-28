# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        def reverse(node):
            nonlocal ans
            if node:
                temp = reverse(node.next)
                node.next = None
                if temp:
                    temp.next = node
                    temp = temp.next
                    return temp
                ans.next = node
                return node
        
        reverse(head)
        return ans.next