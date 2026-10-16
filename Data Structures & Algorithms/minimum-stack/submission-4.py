class MinStack:

    def __init__(self):
        self.stack = []
        self.minvals = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minvals == []:
            self.minvals.append(val)
        elif val <= self.minvals[-1]:
            self.minvals.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minvals[-1]:
            self.minvals.pop()

        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minvals[-1]
