class RandomizedSet:

    def __init__(self):
        self.store = {}
        self.stack = []

    def insert(self, val: int) -> bool:
        if val not in self.store:
            self.stack.append(val)
            self.store[val] = len(self.stack) - 1
            # print(val, self.stack)
            return True
        return False

    def remove(self, val: int) -> bool:
        # print(val, self.store[val])
        if val in self.store:
            i = self.store[val]
            self.store[self.stack[-1]] = i
            self.stack[-1], self.stack[i] = self.stack[i], self.stack[-1]
            # print(self.store[self.stack[-1]])
            self.stack.pop()
            del self.store[val]
            return True
        return False

    def getRandom(self) -> int:
        # print(self.stack)
        return random.choice(self.stack)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()