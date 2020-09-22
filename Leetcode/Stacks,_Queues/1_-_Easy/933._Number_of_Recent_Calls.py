from collections import deque
class RecentCounter:
    def __init__(self):
        self.buffer = deque()
    def ping(self, t: int) -> int:
        while self.buffer and self.buffer[-1]<t-3000:
            self.buffer.pop()
        self.buffer.appendleft(t)
        return len(self.buffer)

#Your RecentCounter object will be instantiated and called as such:

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)