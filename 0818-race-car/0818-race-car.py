class Solution:
    def racecar(self, target: int) -> int:
        queue = deque()
        visited = set()
        queue.append((0,1,0))
        while queue:
            curr_pos, curr_speed, seq = queue.popleft()
            if curr_pos == target:
                return seq
            next_pos, next_speed = curr_pos + curr_speed, curr_speed * 2
            if (next_pos, next_speed) not in visited and abs(target - next_pos) < target:
                queue.append((next_pos, next_speed, seq + 1))
                visited.add((next_pos, next_speed))
            next_pos, next_speed = curr_pos, -1 if curr_speed > 0 else 1
            if (next_pos, next_speed) not in visited and abs(target - next_pos) < target:
                queue.append((next_pos, next_speed, seq + 1))
                visited.add((next_pos, next_speed))
        return -1