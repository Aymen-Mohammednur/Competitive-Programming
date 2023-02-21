class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        final_state = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    queue.append((0, ((i,j), 0)))
                if grid[i][j].islower():
                    final_state |= 1 << (ord(grid[i][j]) - ord("a"))
        
        def isValid(i, j):
            return 0 <= i < m and 0 <= j < n
                
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        visited = set(queue[0])
        while queue:
            current_distance, (position, state) = queue.popleft()
            if state == final_state:
                return current_distance
            for x, y in directions:
                a, b = (position[0] + x, position[1] + y)
                if isValid(a, b) and grid[a][b] != "#":
                    new_state = state
                    if grid[a][b].islower():
                        new_state |= 1 << (ord(grid[a][b]) - ord("a"))
                    elif grid[a][b].isupper() and 1 << (ord(grid[a][b].lower()) - ord("a")) & new_state == 0:
                        continue
                    if ((a, b), new_state) not in visited:
                        queue.append((current_distance + 1, ((a, b), new_state)))
                        visited.add(((a, b), new_state))
        return -1