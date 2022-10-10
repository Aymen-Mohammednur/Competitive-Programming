# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if not root:
            return answer
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
                if i == 0:
                    answer.append(curr.val)
        return answer