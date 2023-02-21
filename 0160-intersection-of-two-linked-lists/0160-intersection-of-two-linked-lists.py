# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def getLen(node):
            count = 0
            while node:
                node = node.next
                count += 1
            return count
        lenA, lenB = getLen(headA), getLen(headB)
        if lenA > lenB:
            diff = lenA - lenB
            for i in range(diff):
                headA = headA.next
        elif lenA < lenB:
            diff = lenB - lenA
            for i in range(diff):
                headB = headB.next
        
        while headA:
            if headA == headB:
                return headA
            headA, headB = headA.next, headB.next
        return None