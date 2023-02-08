class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        counter = Counter()
        for x, y in adjacentPairs:
            graph[x].add(y)
            graph[y].add(x)
            counter[x] += 1
            counter[y] += 1
        
        def dfs(num, prev, ans):
            ans.append(num)
            for adj in graph[num]:
                if prev != adj:
                    dfs(adj, num, ans)
            return ans
        
        for num in counter:
            if counter[num] == 1:
                return dfs(num, None, [])