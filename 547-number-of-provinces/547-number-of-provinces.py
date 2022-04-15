class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.province = n
        
    def find(self, n):
        if self.root[n] == n:
            return n
        self.root[n] = self.find(self.root[n])
        return self.root[n]
    
    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            if self.rank[rootA] > self.rank[rootB]:
                self.root[rootB] = rootA
            elif self.rank[rootA] < self.rank[rootB]:
                self.root[rootA] = rootB
            else:
                self.root[rootA] = rootB
                self.rank[rootB] += 1
            self.province -= 1
                
    def isConnected(self, a, b):
        return self.find(a) == self.find(b)
    
    def getProvince(self):
        return self.province

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        disjoint = UnionFind(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    disjoint.union(i, j)
        return disjoint.getProvince()
    