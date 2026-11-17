class MinStack:

    def __init__(self):
        self.stack = []
        return

    def push(self, val: int) -> None:
        if self.stack and self.stack[-1][1] > val:
            # new min
            self.stack.append((val, val))
        elif self.stack:
            self.stack.append((val, self.stack[-1][1]))
        else:
            # reuse the min at the top
            self.stack.append((val, val))
        return

    def pop(self) -> None:
        self.stack.pop()
        return

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]