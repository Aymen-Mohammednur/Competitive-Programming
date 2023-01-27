class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.val = value
        self.k = k
        self.count = 0

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num == self.val:
            self.count += 1
        else:
            self.count = 0
        if self.count >= self.k:
            return True
        if len(self.queue) < self.k:
            return False
        return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)