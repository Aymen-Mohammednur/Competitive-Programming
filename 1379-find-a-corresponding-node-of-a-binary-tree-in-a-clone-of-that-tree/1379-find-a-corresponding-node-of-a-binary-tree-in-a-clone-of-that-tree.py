# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = deque([cloned])
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.val == target.val:
                    return curr
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        