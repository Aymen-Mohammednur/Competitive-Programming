# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mapping = defaultdict(list)
        queue = deque()
        queue.append([root, 0, 0])        
        while queue:
            node, col, row = queue.popleft()
            mapping[col].append((row, node.val))
            if node.left:
                queue.append([node.left, col-1, row+1])
            if node.right:
                queue.append([node.right, col+1, row+1])    
        output = []
        for col in sorted(mapping.keys()):
            temp = []
            for i in sorted(mapping[col]):
                temp.append(i[1])
            output.append(temp)
        return output