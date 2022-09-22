# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        Sum = 0
        def dfs(node):
            nonlocal Sum
            if node:
                dfs(node.right)
                Sum += node.val
                node.val = Sum
                dfs(node.left)
        dfs(root)
        return root