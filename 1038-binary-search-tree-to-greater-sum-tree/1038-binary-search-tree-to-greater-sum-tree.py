# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def inOrder(node, res):
            if node:
                inOrder(node.left, res)
                res.append(node.val)
                inOrder(node.right, res)
            return res
        res = inOrder(root, [])
        
        mapping = {res[-1] : res[-1]}
        for i in range(len(res) - 2, -1, -1):
            mapping[res[i]] = res[i] + res[i + 1]
            res[i] += res[i + 1]
            
        def inOrder2(node):
            if node:
                inOrder2(node.left)
                node.val = mapping[node.val]
                inOrder2(node.right)
        inOrder2(root)
        return root