class FenwickTree2D:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.bit = [[0] * (m + 1) for _ in range(n + 1)]

    def add(self, x, y, val):
        x += 1
        y += 1
        while x <= self.n:
            y1 = y
            while y1 <= self.m:
                self.bit[x][y1] += val
                y1 += y1 & -y1
            x += x & -x

    def get_sum(self, x, y):
        x += 1
        y += 1
        res = 0
        while x:
            y1 = y
            while y1:
                res += self.bit[x][y1]
                y1 -= y1 & -y1
            x -= x & -x
        return res    

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        fenwick_tree = FenwickTree2D(n, n)
        for q in queries:
            row1, col1, row2, col2 = q
            fenwick_tree.add(row1, col1, 1)
            fenwick_tree.add(row1, col2 + 1, -1)
            fenwick_tree.add(row2 + 1, col1, -1)
            fenwick_tree.add(row2 + 1, col2 + 1, 1)

        mat = [[fenwick_tree.get_sum(i, j) for j in range(n)] for i in range(n)]
        return mat
