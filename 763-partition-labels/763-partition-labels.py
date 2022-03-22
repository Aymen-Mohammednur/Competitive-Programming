class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOcc = {}
        for i in range(len(s)):
            lastOcc[s[i]] = i
        visited = set()
        output = []
        count = 0
        for i in range(len(s)):
            count += 1
            visited.add(s[i])
            if lastOcc[s[i]] == i:
                visited.remove(s[i])
                if len(visited) == 0:
                    output.append(count)
                    count = 0
        return output