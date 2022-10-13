# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], l = float('-inf'), r = float('inf')) -> bool:
        if not root:
            return True
        if not l < root.val < r:
            return False
        left = self.isValidBST(root.left, l, root.val)
        right = self.isValidBST(root.right, root.val, r)
        return left and right