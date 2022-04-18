# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        def inOrder(node):
            if node:
                inOrder(node.left)
                heappush(heap, node.val)
                inOrder(node.right)
        inOrder(root)
        for i in range(k - 1):
            heappop(heap)
        return heap[0]