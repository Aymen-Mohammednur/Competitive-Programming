# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        Dict = {}
        prefix = 0
        index = 0
        while curr:
            prefix += curr.val
            index += 1
            if prefix == 0:
                head = curr.next
                Dict = {}
            elif prefix in Dict:
                node = Dict[prefix][0]
                node.next = curr.next
                temp = {}
                for key in Dict.keys():
                    if Dict[key][1] <= Dict[prefix][1]:
                        temp[key] = Dict[key]
                Dict = temp
            else:
                Dict[prefix] = [curr, index]
            curr = curr.next
        return head