class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        store = defaultdict(set)
        ans = [0 for i in range(k)]
        for id, time in logs:
            store[id].add(time)
        for times in store.values():
            ans[len(times) - 1] += 1
        return ans