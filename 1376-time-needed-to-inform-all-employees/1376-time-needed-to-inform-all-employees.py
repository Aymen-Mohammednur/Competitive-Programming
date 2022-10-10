class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(set)
        for i in range(len(manager)):
            if manager[i] == -1:
                continue
            graph[manager[i]].add(i)
        maxTime = 0
        def dfs(employee, time):
            nonlocal maxTime
            maxTime = max(maxTime, time)
            for sub in graph[employee]:
                dfs(sub, time + informTime[employee])
                
        dfs(headID, 0)
        return maxTime
