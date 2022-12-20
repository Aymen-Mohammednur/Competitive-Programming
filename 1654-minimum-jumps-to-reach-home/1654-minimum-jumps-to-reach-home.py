class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        queue = deque()
        queue.append([0, False, 0])
        forbidden = set(forbidden)
        visited = set()
        while queue:
            curr_jump, backward, count = queue.popleft()
            if curr_jump == x:
                return count
            if backward:
                if curr_jump - b not in forbidden and curr_jump - b not in visited and curr_jump - b > 0:
                    queue.append([curr_jump - b, False, count + 1])
                    visited.add(curr_jump - b )
            if curr_jump + a not in forbidden and curr_jump + a not in visited and curr_jump + a <= max(x, max(forbidden)) + a + b:
                queue.append([curr_jump + a, True, count + 1])
                visited.add(curr_jump + a)
        return -1