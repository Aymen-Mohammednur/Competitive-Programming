class Solution:
    def getTimeInMinutes(self, time):
        hour, minute = time.split(":")
        hour = int(hour)
        minute = int(minute)
        return hour * 60 + minute
    
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        mapping = defaultdict(list)
        for i in range(len(keyName)):
            time = self.getTimeInMinutes(keyTime[i])
            mapping[keyName[i]].append(time)
        res = []
        for name in mapping:
            times = mapping[name]
            times.sort()
            queue = deque()
            for time in times:
                while queue and time - queue[0] > 60:
                    queue.popleft()
                queue.append(time)
                if len(queue) >= 3:
                    res.append(name)
                    break
        return sorted(res)