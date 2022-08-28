class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        for i in range(len(tickets)):
            queue.append(i)
        time = 0
        while queue:
            i = queue.popleft()
            tickets[i] -= 1
            time += 1
            if i == k and tickets[i] == 0:
                return time
            if tickets[i] != 0:
                queue.append(i)
        return time