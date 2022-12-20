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
            l = 0
            for r in range(2, len(times)):
                if times[r] - times[l] <= 60:
                    res.append(name)
                    break
                l += 1
        return sorted(res)