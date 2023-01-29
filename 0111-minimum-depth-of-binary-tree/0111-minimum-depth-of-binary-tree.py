# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def min_depth(root, res, depth):
            if not root.left and not root.right:
                res[0] = min(res[0], depth)
            if root.left:
                min_depth(root.left, res, depth + 1)
            if root.right:
                min_depth(root.right, res, depth + 1)
            return res
        return min_depth(root, [float('inf')], 1)[0]