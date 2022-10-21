class RandomizedCollection:

    def __init__(self):
        self.store = defaultdict(set)
        self.array = []

    def insert(self, val: int) -> bool:
        self.array.append(val)
        self.store[val].add(len(self.array) - 1)
        return len(self.store[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.store[val]:
            return False
        remove = self.store[val].pop()
        last = self.array[-1]
        self.array[remove] = last
        self.store[last].add(remove)
        self.store[last].remove(len(self.array) - 1)
        self.array.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.array)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()