# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        ans = 0
        def inOrder(node):
            nonlocal ans, count
            if node:
                inOrder(node.left)
                count += 1
                if count == k:
                    ans = node.val
                    return
                inOrder(node.right)
        inOrder(root)
        return ans