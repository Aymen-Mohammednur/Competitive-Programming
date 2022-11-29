"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        queue = deque([node])
        clone = Node(node.val, [])
        cloned = { clone.val : clone }
        while queue:
            curr = queue.popleft()
            curr_clone = cloned[curr.val]
            for neigh in curr.neighbors:
                if neigh.val not in cloned:
                    queue.append(neigh)
                    cloned[neigh.val] = Node(neigh.val, [])
                curr_clone.neighbors.append(cloned[neigh.val])
        return cloned[node.val]