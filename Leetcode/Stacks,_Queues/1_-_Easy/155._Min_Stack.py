from collections import deque
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = deque()

    def push(self, x: int) -> None:
        m = self.stack[-1][1] if self.stack else None
        if not self.stack or x<m:
            m = x
        self.stack.append((x,m))
        
    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()