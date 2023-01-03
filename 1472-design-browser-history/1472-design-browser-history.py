class BrowserHistory:

    def __init__(self, homepage: str):
        self.backward = [homepage]
        self.forward_stack = []

    def visit(self, url: str) -> None:
        self.backward.append(url)
        self.forward_stack = []

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if len(self.backward) > 1:
                self.forward_stack.append(self.backward.pop())
        return self.backward[-1]

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.forward_stack:
                self.backward.append(self.forward_stack.pop())
        return self.backward[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)