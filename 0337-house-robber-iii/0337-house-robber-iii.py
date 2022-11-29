# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(node, picked):
            if not node:
                return 0
            pick = node.val + dfs(node.left, True) + dfs(node.right, True) if not picked else 0
            not_pick = dfs(node.left, False) + dfs(node.right, False)
            return max(pick, not_pick)
        return dfs(root, False)