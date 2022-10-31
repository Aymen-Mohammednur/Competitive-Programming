class UnionFind:
    def __init__(self):
        self.parent = [i for i in range(1001)]
        self.size = [1] * 1001
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        # this edge can be deleted
        if parent1 == parent2:
            return True
        if self.size[node1] >= self.size[node2]:
            self.parent[parent2] = parent1
            self.size[parent2] += self.size[parent1]
        else:
            self.parent[parent1] = parent2
            self.size[parent1] += self.size[parent2]
        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        disjoint = UnionFind()
        ans = None
        for edge in edges:
            if disjoint.union(edge[0], edge[1]):
                ans = edge
        return ans