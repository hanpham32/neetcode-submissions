class MinStack:

    def __init__(self):
        self.stack = []
        return

    def push(self, val: int) -> None:
        newMin = val
        if self.stack:
            newMin = min(val, self.stack[-1][1])
        self.stack.append((val, newMin))
        return

    def pop(self) -> None:
        self.stack.pop()
        return

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]