# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], low = -inf, high = inf) -> bool:
        if not root:
            return True
        if root.val <= low or root.val >= high:
            return False
        left = self.isValidBST(root.left, low, root.val)
        right = self.isValidBST(root.right, root.val, high)
        return left and right