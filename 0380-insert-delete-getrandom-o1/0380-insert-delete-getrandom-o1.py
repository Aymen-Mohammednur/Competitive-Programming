import random
class RandomizedSet:

    def __init__(self):
        self.store = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val not in self.store:
            self.nums.append(val)
            self.store[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.store:
            num_index = self.store[val]
            last_num = self.nums[-1]
            self.store[last_num] = num_index
            self.nums[num_index], self.nums[-1] = self.nums[-1], self.nums[num_index]
            self.nums.pop()
            del self.store[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()