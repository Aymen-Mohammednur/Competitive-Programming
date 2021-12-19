# LEETCODE 232
# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2 and self.stack1:
            while(self.stack1):
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return self.stack2.pop()

    def peek(self) -> int:
        return self.stack1[0] if self.stack1 else self.stack2[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0

myQueue = MyQueue()
myQueue.push(1)  # queue is: [1]
myQueue.push(2)  # // queue is: [1, 2] (leftmost is front of the queue)
print(myQueue.peek()) # // return 1
print(myQueue.pop())  # // return 1, queue is [2]
print(myQueue.empty())  # // return false
