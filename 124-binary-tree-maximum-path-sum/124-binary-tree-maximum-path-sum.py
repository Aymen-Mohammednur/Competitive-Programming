# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')
        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0
            sumLeft = max(dfs(node.left), 0)
            sumRight = max(dfs(node.right), 0)
            sumNode = node.val + sumLeft + sumRight
            maxSum = max(maxSum, sumNode)
            
            return node.val + max(sumLeft, sumRight)
        dfs(root)
        return maxSum