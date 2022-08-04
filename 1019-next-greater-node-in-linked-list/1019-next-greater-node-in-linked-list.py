# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        monoStack = []
        index = 0
        dummy = head
        result = []
        while dummy:
            result.append(0)
            while monoStack and dummy.val > monoStack[-1][0]:
                result[monoStack.pop()[1]] = dummy.val
            monoStack.append([dummy.val, index])
            dummy = dummy.next
            index += 1
        return result