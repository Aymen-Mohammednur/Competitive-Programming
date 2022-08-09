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
        if not head:
            return
        curr = head
        res = Node()
        dummy = res
        stack = []
        def dfs(curr):
            nonlocal dummy
            curr.prev = dummy
            dummy.next = curr
            dummy = dummy.next
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                dfs(curr.child)
                curr.child = None
            else:
                if curr.next:
                    dfs(curr.next)
                else:
                    if stack:
                        dfs(stack.pop())
        dfs(curr)
        res = res.next
        res.prev = None
        return res