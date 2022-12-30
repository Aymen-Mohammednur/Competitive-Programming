class OrderedStream:

    def __init__(self, n: int):
        self.curr_ptr = 1
        self.store = {}

    def insert(self, idKey: int, value: str) -> List[str]:
        self.store[idKey] = value
        res = []
        while self.store.get(self.curr_ptr):
            res.append(self.store[self.curr_ptr])
            self.curr_ptr += 1
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)