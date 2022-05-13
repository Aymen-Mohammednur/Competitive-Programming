"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = deque()
        queue.append(root)
        while queue:
            for _ in range(len(queue) - 1):
                curr = queue.popleft()
                curr.next = queue[0] if queue else None
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return root