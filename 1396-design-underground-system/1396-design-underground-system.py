class UndergroundSystem:

    def __init__(self):
        self.store = {}
        self.average = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.store[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin_station, checkin_time = self.store[id]
        avg = t - checkin_time
        if (checkin_station, stationName) in self.average:
            prev_avg, length = self.average[(checkin_station, stationName)]
            prev_sum = prev_avg * length
            new_avg = (prev_sum + avg) / (length + 1)
            self.average[(checkin_station, stationName)] = [new_avg, length + 1]
        else:
            self.average[(checkin_station, stationName)] = [avg, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.average[(startStation, endStation)][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)