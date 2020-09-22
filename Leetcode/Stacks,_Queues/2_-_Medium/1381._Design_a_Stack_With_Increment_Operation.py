from collections import deque
class CustomStack:

    def __init__(self, maxSize: int):
        self.buffer = deque()
        self.max = maxSize

    def push(self, x: int) -> None:
        if len(self.buffer)<self.max:
            self.buffer.append(x)

    def pop(self) -> int:
        if self.buffer:
            return self.buffer.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        queue = deque()
        while self.buffer and len(self.buffer)>k:
            queue.append(self.buffer.pop())
        while self.buffer:
            queue.append(self.buffer.pop()+val)
        while queue:
            self.buffer.append(queue.pop())
        

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)