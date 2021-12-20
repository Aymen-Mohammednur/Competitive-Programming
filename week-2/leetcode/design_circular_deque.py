# LEETCODE 641
# https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:
    def __init__(self, k: int):
        self.deque = [None] * k
        self.front = 0
        self.last = 0
        self.count = 0
        self.len = len(self.deque)

    def insertFront(self, value: int) -> bool:
        if (self.isFull()):
            return False
        else:
            if (self.count < 1):
                self.deque[self.front % self.len] = value
            else:
                self.front -= 1
                self.deque[self.front % self.len] = value
            self.count += 1
            return True

    def insertLast(self, value: int) -> bool:
        if (self.isFull()):
            return False
        else:
            if (self.count < 1):
                self.deque[self.last % self.len] = value
            else:
                self.last += 1
                self.deque[self.last % self.len] = value
            self.count += 1
            return True

    def deleteFront(self) -> bool:
        if (self.isEmpty()):
            return False
        else:
            self.deque[self.front % self.len] = None
            self.front += 1
            self.count -= 1
            if self.count == 0:
                self.front = 0
                self.last = 0
            return True

    def deleteLast(self) -> bool:
        if (self.isEmpty()):
            return False
        else:
            self.deque[self.last % self.len] = None
            self.last -= 1
            self.count -= 1
            if self.count == 0:
                self.front =0
                self.last = 0
            return True

    def getFront(self) -> int:
        if (self.isEmpty()):
            return -1
        else:
            return self.deque[self.front]

    def getRear(self) -> int:
        if (self.isEmpty()):
            return -1
        else:
            return self.deque[self.last]

    def isEmpty(self) -> bool:
        return True if self.count == 0 else False

    def isFull(self) -> bool:
        return True if self.count == self.len else False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()