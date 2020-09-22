from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.tops = None
        
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.tops = x
        self.queue.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        temp = deque()
        while len(self.queue)>1:
            temp.append(self.queue.popleft())
        ret = self.queue.popleft()
        self.tops = None
        while temp:
            self.tops = temp.popleft()
            self.queue.append(self.tops)
        return ret

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.tops

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()