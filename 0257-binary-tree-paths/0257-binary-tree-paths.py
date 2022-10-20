# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        def dfs(root, path):
            if not root.left and not root.right:
                path.append(str(root.val))
                paths.append(path.copy())
            else:
                path.append(str(root.val) + '->')
            if root.left:
                dfs(root.left, path)
            if root.right:
                dfs(root.right, path)
            path.pop()
        dfs(root, [])
        res = []
        for path in paths:
            p = "".join(path)
            res.append(p)
        return res