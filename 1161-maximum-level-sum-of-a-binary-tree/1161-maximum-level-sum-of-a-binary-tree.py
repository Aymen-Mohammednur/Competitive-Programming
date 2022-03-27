# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        maxLevel, level = 1, 1
        maxSum = -float("inf")
        while queue:
            Sum = 0
            for i in range(len(queue)):
                current = queue.popleft()
                Sum += current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            if Sum > maxSum:
                maxSum = Sum
                maxLevel = level
            level += 1
        return maxLevel