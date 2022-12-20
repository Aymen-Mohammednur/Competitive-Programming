class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        exits = set()
        
        def inBound(r, c):
            return 0 <= r < rows and 0 <= c < cols

        # Find the indexes of the cells on the top and bottom row
        for j in range(cols):
            if maze[0][j] == '.': exits.add((0, j))
            if maze[rows-1][j] == '.': exits.add((rows - 1, j))

        # Find the indexes of the cells on the left and right column
        for i in range(1, rows - 1):
            if maze[i][0] == '.': exits.add((i, 0))
            if maze[i][cols-1] == '.': exits.add((i, cols - 1))
        
        if (entrance[0], entrance[1]) in exits:
            exits.remove((entrance[0], entrance[1]))
        
        if not exits: return -1
        
        queue = deque()
        queue.append([entrance[0], entrance[1], 0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        visited.add((entrance[0], entrance[1]))
        while queue:
            r, c, steps = queue.popleft()
            if (r, c) in exits:
                return steps
            for x, y in directions:
                nr, nc = x+r, y+c
                if inBound(nr, nc) and (nr, nc) not in visited and maze[nr][nc] == '.':
                    queue.append([nr,nc,steps + 1])
                    visited.add((nr,nc))
        return -1