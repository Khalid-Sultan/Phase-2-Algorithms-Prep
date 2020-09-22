from collections import deque
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buffer = deque()
        self.front = None
        
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.buffer:
            self.front = x
        self.buffer.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.buffer: return None
        self.temp = deque()
        while self.buffer:
            self.temp.append(self.buffer.pop())
        val = self.temp.pop()
        self.front = self.temp[-1] if self.temp else None
        while self.temp:
            self.buffer.append(self.temp.pop())
        return val
    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.front        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.buffer)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()