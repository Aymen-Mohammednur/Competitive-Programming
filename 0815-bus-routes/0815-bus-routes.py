class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """
        1,2,3    3,5  5,6
        """
        if source == target:
            return 0
        graph = defaultdict(set)
        for i in range(len(routes)):
            route = routes[i]
            for stop in route:
                graph[stop].add(i)
        queue = deque()
        visited_stops = set()
        visited_routes = set()
        for route in graph[source]:
            queue.append([routes[route], 1])
        visited_stops.add(source)
        while queue:
            curr_route, curr_buses = queue.popleft()
            for stop in curr_route:
                if stop == target:
                    return curr_buses
                if stop in visited_stops:
                    continue
                visited_stops.add(stop)
                for route in graph[stop]:
                    if route not in visited_routes:
                        queue.append([routes[route], curr_buses + 1])
                        visited_routes.add(route)
        return -1