class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for i in range(len(self.calendar)):
            if start < self.calendar[i][1] and self.calendar[i][0] < end:
                return False
        self.calendar.append([start, end])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)