class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        n = self._getStackLastIdx() - 1
        del self.stack[n]

    def top(self) -> int:
        n = self._getStackLastIdx() - 1
        return self.stack[n]

    def getMin(self) -> int:
        return min(self.stack)

    def _getStackLastIdx(self) -> int:
        return len(self.stack)
        
