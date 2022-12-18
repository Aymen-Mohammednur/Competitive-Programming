class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        original = image[sr][sc]
        def inBound(r, c):
            return 0 <= r < n and 0 <= c < m
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        def dfs(i, j):
            visited.add((i, j))
            image[i][j] = color
            for x, y in directions:
                nr, nc = i + x, j + y
                if inBound(nr, nc) and (nr, nc) not in visited and image[nr][nc] == original:
                    dfs(nr, nc)
        dfs(sr, sc)
        return image