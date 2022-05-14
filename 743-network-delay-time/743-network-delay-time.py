class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        totalTime = 0
        minHeap = [(0, k)]
        visited = set()
        
        while minHeap and len(visited) < n:
            time, node = heappop(minHeap)
            visited.add(node)
            totalTime = max(totalTime, time)
            for node2, time2 in graph[node]:
                if node2 not in visited:
                    heappush(minHeap, (time2 + time, node2))
                    
        return totalTime if len(visited) == n else -1