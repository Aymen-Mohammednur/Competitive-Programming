class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))
        queue = deque()
        queue.append((src, 0))
        costs = [float('inf')] * n
        while queue and k >= 0:
            l = len(queue)
            for _ in range(l):
                curr_flight, curr_cost = queue.popleft()
                for next_flight, next_cost in graph[curr_flight]:
                    if curr_cost + next_cost < costs[next_flight]:
                        costs[next_flight] = curr_cost + next_cost
                        queue.append((next_flight, costs[next_flight]))
            k -= 1
        return costs[dst] if costs[dst] != float('inf') else -1