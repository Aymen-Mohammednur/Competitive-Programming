# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        leftSum = 0
        def traverse(root, isLeft):
            nonlocal leftSum
            if not root:
                return 0
            if not root.left and not root.right:
                if isLeft:
                    leftSum += root.val
                return
            traverse(root.left, True)
            traverse(root.right, False)
        traverse(root, False)
        return leftSum