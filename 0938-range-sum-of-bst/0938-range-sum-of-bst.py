# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = [0]
        def dfs(root, res):
            if not root:
                return 0
            dfs(root.left, res)
            if low <= root.val <= high:
                res[0] += root.val
            dfs(root.right, res)
        dfs(root, res)
        return res[0]